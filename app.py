import pickle
from flask import Flask, request, render_template
import random  # Used to simulate job count

app = Flask(__name__)

# ✅ Load trained model from file
def load_model():
    try:
        with open('model/career_model.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("❌ Model not found.")
        return None

model_package = load_model()
# ✅ Normalize text
def normalize(text):
    return text.lower().replace('-', ' ').strip()

# ✅ Simulated Job Count Lookup (you can replace this later with real API or scraped data)
def fetch_job_count(career):
    simulated_counts = {
        "data scientist": 1300,
        "project manager": 900,
        "mobile app developer": 1100,
        "frontend developer": 1000,
        "backend developer": 980,
    }
    return simulated_counts.get(career.lower(), random.randint(200, 1000))

# ✅ Normalize job demand score (0.0 to 1.0)
def normalize_demand(count, min_jobs=50, max_jobs=2000):
    return min(1.0, max(0.0, (count - min_jobs) / (max_jobs - min_jobs)))

# ✅ Predict top 1 career with job demand enhancement
def predict_career(interests, skills):
    if model_package is None:
        return [("Model not loaded", 0.0)]

    # Normalize input
    combined = []
    if isinstance(interests, str):
        combined += [normalize(x) for x in interests.split(',') if x.strip()]
    if isinstance(skills, str):
        combined += [normalize(x) for x in skills.split(',') if x.strip()]

    print(f"DEBUG: Normalized input features: {combined}")

    known_features = set(normalize(f) for f in model_package['feature_names'])
    filtered = [f for f in combined if f in known_features]

    print(f"DEBUG: Filtered input features: {filtered}")

    # Encode input
    mlb = model_package['feature_encoder']
    X = mlb.transform([filtered])

    model = model_package['classifier']
    proba = model.predict_proba(X)[0]
    careers = model.classes_

    top_indices = proba.argsort()[-5:][::-1]
    top_preds = [(careers[i], round(proba[i] * 100, 2)) for i in top_indices]

    # Enhance with job demand
    hybrid_scores = []
    for career, conf in top_preds:
        job_count = fetch_job_count(career)
        demand_score = normalize_demand(job_count)
        final_score = round(0.7 * (conf / 100) + 0.3 * demand_score, 4)
        hybrid_scores.append((career, round(final_score * 100, 2)))

    # Return only top 1
    return sorted(hybrid_scores, key=lambda x: x[1], reverse=True)[:1]

# ✅ Route: Home page
@app.route('/')
def home():
    return render_template('form.html')

# ✅ Route: Form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    interests = request.form['interest']
    skills = request.form['skills']
    qualification = request.form['qualification']
    career_pref = request.form['career_pref']

    predictions = predict_career(interests, skills)
    top_career, confidence = predictions[0]

       # ✅ Get the description for the predicted career (normalized)
    description_dict = model_package.get('descriptions', {})
    description = description_dict.get(top_career.lower(), "Description not available for this career.")

    # Process user input
    interests_list = [x.strip() for x in interests.split(',') if x.strip()]
    skills_list = [x.strip() for x in skills.split(',') if x.strip()]

    return render_template('result.html',
                           name=name,
                           interests=', '.join(interests_list),
                           skills=', '.join(skills_list),
                           qualification=qualification,
                           career_pref=career_pref,
                           career=top_career,
                           confidence=confidence,
                           description=description)

# ✅ Run app
if __name__ == '__main__':
    app.run(debug=True)
