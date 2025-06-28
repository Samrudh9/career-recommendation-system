import re

def analyze_resume(text):
    skills = set()
    suggestions = []
    careers = []

    # Dummy skills list for matching
    known_skills = [
        "python", "sql", "html", "css", "javascript",
        "flask", "java", "c++", "tensorflow", "pandas", "machine learning"
    ]
    lower_text = text.lower()

    # Extract skills
    for skill in known_skills:
        if skill in lower_text:
            skills.add(skill)

    if not skills:
        suggestions.append("Include more technical or relevant skills.")
    if "internship" not in lower_text:
        suggestions.append("Add internship experience if available.")
    if "project" not in lower_text:
        suggestions.append("Mention key academic or personal projects.")

    # Basic career suggestion
    if "machine learning" in skills or "tensorflow" in skills:
        careers.append("Machine Learning Engineer")
    elif "flask" in skills:
        careers.append("Backend Developer")
    elif "html" in skills and "css" in skills:
        careers.append("Frontend Developer")
    else:
        careers.append("Software Developer")

    return {
        "skills": list(skills),
        "careers": careers,
        "suggestions": suggestions
    }