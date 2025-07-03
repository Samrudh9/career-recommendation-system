import os
import sys
import pickle
import random
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from analyzer.resume_parser import extract_text_from_pdf
from analyzer.resume_analyzer import analyze_resume
from analyzer.quality_checker import check_resume_quality
from analyzer.resource_recommender import recommend_resources
from analyzer.salary_estimator import salary_est

app = Flask(__name__)

# ===== Configuration =====
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ===== Load Trained Model =====
def load_model():
    try:
        with open('model/career_model.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("❌ Model not found.")
        return None

model_package = load_model()

# ===== Utility Functions =====
def normalize(text):
    return text.lower().replace('-', ' ').strip()

def fetch_job_count(career):
    simulated_counts = {
        "data scientist": 1300,
        "project manager": 900,
        "mobile app developer": 1100,
        "frontend developer": 1000,
        "backend developer": 980,
    }
    return simulated_counts.get(career.lower(), random.randint(200, 1000))

def normalize_demand(count, min_jobs=50, max_jobs=2000):
    return min(1.0, max(0.0, (count - min_jobs) / (max_jobs - min_jobs)))

def predict_career(interests, skills):
    if model_package is None:
        return [("Model not loaded", 0.0)]

    combined = []
    if isinstance(interests, str):
        combined += [normalize(x) for x in interests.split(',') if x.strip()]
    if isinstance(skills, str):
        combined += [normalize(x) for x in skills.split(',') if x.strip()]

    known_features = set(normalize(f) for f in model_package['feature_names'])
    filtered = [f for f in combined if f in known_features]

    mlb = model_package['feature_encoder']
    X = mlb.transform([filtered])

    model = model_package['classifier']
    proba = model.predict_proba(X)[0]
    careers = model.classes_

    top_indices = proba.argsort()[-5:][::-1]
    top_preds = [(careers[i], round(proba[i] * 100, 2)) for i in top_indices]

    hybrid_scores = []
    for career, conf in top_preds:
        job_count = fetch_job_count(career)
        demand_score = normalize_demand(job_count)
        final_score = round(0.7 * (conf / 100) + 0.3 * demand_score, 4)
        hybrid_scores.append((career, round(final_score * 100, 2)))

    return sorted(hybrid_scores, key=lambda x: x[1], reverse=True)[:3]

# ===== Routes =====
@app.route('/')
def home():
    return render_template('intro.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    interests = request.form['interest']
    skills = request.form['skills']
    qualification = request.form['qualification']
    career_pref = request.form.get('career_pref', '').strip()

    predictions = predict_career(interests, skills)
    description_dict = model_package.get('descriptions', {})

    top_3_careers = []
    for career, confidence in predictions:
        description = description_dict.get(career) or \
                      description_dict.get(career.lower()) or \
                      "Description not available for this career."
        top_3_careers.append({
            'career': career,
            'confidence': confidence,
            'description': description
        })

    interests_list = [x.strip() for x in interests.split(',') if x.strip()]
    skills_list = [x.strip() for x in skills.split(',') if x.strip()]

    return render_template('result.html',
                           name=name,
                           interests=', '.join(interests_list),
                           skills=', '.join(skills_list),
                           qualification=qualification,
                           career_pref=career_pref,
                           top_3_careers=top_3_careers)

# ===== Resume Upload Page =====
@app.route('/upload')
def upload():
    return render_template('upload_form.html')

@app.route('/resume', methods=['POST'])
def handle_resume_upload():
    resume = request.files['resume']
    qualification = request.form.get('qualification', 'Unknown')

    if not resume or resume.filename == '':
        return "❌ No resume uploaded", 400

    filename = secure_filename(resume.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    resume.save(filepath)

    extracted_text = extract_text_from_pdf(filepath)
    analysis = analyze_resume(extracted_text)
    skills_found = analysis.get("skills", [])
    resume_score = analysis.get("score", 60)

    skills_text = ', '.join(skills_found)
    predictions = predict_career("", skills_text)

    top_3_careers = []
    description_dict = model_package.get('descriptions', {})
    for career, confidence in predictions:
        description = description_dict.get(career) or \
                      description_dict.get(career.lower()) or \
                      "Description not available for this career."
        top_3_careers.append({
            'career': career,
            'confidence': confidence,
            'description': description
        })

    salary_value, _ = salary_est.estimate(
        skills=skills_text,
        career=predictions[0][0],
        qualification=qualification
    )
    predicted_salary = f"₹{salary_value:,}/year"

    quality_feedback = check_resume_quality(analysis.get("missing", []))
    resources = recommend_resources(predictions[0][0])

    return render_template('resume_result.html',
                           skills=skills_text,
                           resume_score=resume_score,
                           predicted_salary=predicted_salary,
                           quality_feedback=quality_feedback,
                           resources=resources,
                           top_3_careers=top_3_careers)

# ===== Run =====
if __name__ == '__main__':
    app.run(debug=True)
