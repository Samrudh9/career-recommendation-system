# Career Recommendation System Using Machine Learning

## 🎯 Objective
To build a machine learning-based web application that provides personalized career suggestions to users based on their interests, skills, and preferences. The system uses a trained classification model to match user input with suitable career paths.

## 💡 Motivation
Many students and early professionals struggle to choose the right career. Our project aims to provide data-driven recommendations, acting as a virtual career counselor. This tool can reduce uncertainty and support informed decision-making.

## 🔍 Scope
- Collect and preprocess user input data (skills, interests, academic scores).
- Train an ML model to classify user profiles into career categories.
- Build a Flask-based web application for user interaction.
- Display the top 3–5 career suggestions with brief descriptions.
- Deploy the system using Replit or PythonAnywhere.

## 🧪 Methodology

### 1. Data Collection
- Use open datasets or manually created CSV with features like subject interest, technical/non-technical skills, preferred domains, etc.
- Perform cleaning and encoding (e.g., label encoding, one-hot encoding).

### 2. Model Development
- Train using classification algorithms: Decision Tree, Random Forest, or Logistic Regression.
- Evaluate with metrics like accuracy and F1-score.
- Save the model as `model.pkl` using `joblib`.

### 3. Web Application
- Use Flask to create routes and serve HTML pages.
- Create a simple frontend using HTML/CSS for user input and output.
- Integrate ML model to predict careers based on submitted data.

### 4. Testing
- Validate predictions with different inputs.
- Handle incorrect inputs and provide feedback.
- Ensure UI responsiveness and usability.

## 🛠️ Tools and Technologies
- **Languages:** Python, HTML, CSS
- **Libraries:** Scikit-learn, Pandas, Numpy, Joblib
- **Framework:** Flask
- **Visualization:** Matplotlib, Seaborn
- **Collaboration:** GitHub, Google Drive, Replit Teams
- **Deployment:** Replit / PythonAnywhere

## ⚠️ Challenges and Solutions
| Challenge | Solution |
|----------|----------|
| Small or imbalanced dataset | Use synthetic data or expand dataset manually |
| Model underperformance | Try different algorithms and tune hyperparameters |
| New team to tech stack | Use beginner-friendly tools and tutorials |
| Remote collaboration | Use shared drives, Trello, and Replit for version control |

## 🎯 Expected Outcome
- A responsive web app that collects user input and provides top career suggestions.
- A trained ML model with decent prediction accuracy.
- A structured codebase and clean UI.
- A complete report documenting the process, learnings, and future scope.

## 👥 Team Member Roles

| Member | Role | Responsibility |
|--------|------|----------------|
| A | ML Engineer & Team Lead | Dataset, model training, guidance |
| B | Backend Developer | Flask routes, model integration |
| C | Frontend Developer | HTML form, result display, CSS |
| D | Tester & Debugger | Input validation, UI testing |
| E | Documentation & UI Design | Report writing, slides, UI tweaks |

## 🗓️ 4-Week Timeline

| Week | Tasks |
|------|--------|
| **Week 1** | Finalize project, assign roles, setup tools, collect dataset, preprocessing |
| **Week 2** | Train model, evaluate, begin Flask backend and HTML form |
| **Week 3** | Model integration, form connection, result display, testing |
| **Week 4** | Final fixes, deployment, prepare report, slide deck, and submit |

## ✅ How to Run
1. Clone or fork this repository.
2. Install dependencies: `pip install -r REQUIREMENTS.txt`
3. Run the Flask app: `python app.py`
4. Open browser at `http://localhost:5000/` to interact with the app.

## 📚 References
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Career Dataset - Kaggle](https://www.kaggle.com/)
- Online ML Tutorials (YouTube, ChatGPT)
