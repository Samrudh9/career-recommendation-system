import re

def check_resume_quality(text):
   
    score = 100
    tips = []
    text_lower = text.lower()

    # 1. Contact Information
    if not re.search(r"\b[\w.-]+@[\w.-]+\.[a-z]{2,}\b", text_lower):
        tips.append("Add a professional email address.")
        score -= 10
    if not re.search(r"\b\+?\d{10,15}\b", text_lower):
        tips.append("Include a valid phone number with country code.")
        score -= 10

    # 2. Section Headings
    required_sections = ["experience", "education", "skills", "projects", "certifications"]
    missing = [s for s in required_sections if not re.search(rf"^{s}[:\s]", text_lower, re.MULTILINE)]
    if missing:
        tips.append(f"Missing sections: {', '.join([s.title() for s in missing])}.")
        score -= 5 * len(missing)

    # 3. Action Verbs & Tone
    action_verbs = ["achieved", "designed", "implemented", "optimized", "led", "managed"]
    found_verbs = sum(1 for v in action_verbs if v in text_lower)
    if found_verbs < 3:
        tips.append("Use more strong action verbs (e.g., Led, Implemented, Optimized).")
        score -= 10

    # 4. Quantifiable Achievements
    if not re.search(r"\d+%|\d+\s+(?:million|k|thousand)", text_lower):
        tips.append("Quantify achievements with metrics (e.g., Increased revenue by 20%).")
        score -= 10

    # 5. Trending Technologies
    trending = ["cloud", "docker", "kubernetes", "aws", "azure", "gcp", "machine learning", "data science"]
    matched = [t for t in trending if t in text_lower]
    if not matched:
        tips.append("Mention trending industry technologies (e.g., AWS, Docker, Kubernetes).")
        score -= 5

    # 6. Formatting Consistency (bullets)
    bullet_style = re.findall(r"^[-*+]\s+", text, re.MULTILINE)
    if not bullet_style:
        tips.append("Use consistent bullet points for lists of responsibilities and achievements.")
        score -= 5

    # 7. Length & Readability
    if len(text) < 700:
        tips.append("Consider expanding sections for clarity; aim for 1-2 pages.")
        score -= 5

    # Cap score
    score = max(0, min(100, score))

    if score >= 85 and not tips:
        tips.append("Excellent! Your resume follows modern industry standards.")

    return {"score": score, "tips": tips}