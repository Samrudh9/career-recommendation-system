def check_resume_quality(text):
    quality_issues = []

    if len(text) < 200:
        quality_issues.append("Resume is too short.")

    if not any(keyword in text.lower() for keyword in ["experience", "projects", "education", "skills"]):
        quality_issues.append("Resume may be missing important sections (e.g., Experience, Skills, Education).")

    if 'lorem ipsum' in text.lower():
        quality_issues.append("Placeholder text found in resume.")

    return quality_issues if quality_issues else ["Resume quality looks good!"]