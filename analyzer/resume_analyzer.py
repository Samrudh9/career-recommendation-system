
import re
import pandas as pd

# Path to your CSV file with skill-career pairs
SKILL_DB_PATH = "dataset/skills_career_map.csv"  # Must have columns: skill, career

# ===== Load CSV into dictionary =====
def load_skill_career_map():
    df = pd.read_csv(SKILL_DB_PATH)
    skill_to_career = {}
    for _, row in df.iterrows():
        skill = row['skill'].strip().lower()
        career = row['career'].strip()
        skill_to_career.setdefault(skill, set()).add(career)
    return skill_to_career

# ===== Global skill-career map =====
SKILL_CAREER_MAP = load_skill_career_map()
ALL_KNOWN_SKILLS = list(SKILL_CAREER_MAP.keys())

# ===== Extract matched skills =====
def extract_skills(text):
    found_skills = set()
    text = text.lower()
    for skill in ALL_KNOWN_SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found_skills.add(skill)
    return found_skills

# ===== Rank top careers =====
def match_careers_from_skills(skills_found):
    career_counter = {}
    for skill in skills_found:
        careers = SKILL_CAREER_MAP.get(skill, [])
        for career in careers:
            career_counter[career] = career_counter.get(career, 0) + 1

    # Rank by most overlapping skills
    total_skills = len(skills_found)
    sorted_careers = sorted(career_counter.items(), key=lambda x: x[1], reverse=True)
    career_matches = [(career, round((count / total_skills) * 100, 1)) for career, count in sorted_careers]
    return career_matches[:3]  # return top 3 matches

# ===== Analyze complete resume text =====
def analyze_resume(text):
    suggestions = []
    lower_text = text.lower()

    # Extract matched skills
    skills = extract_skills(lower_text)

    # Suggestions
    if not skills:
        suggestions.append("Include more technical or relevant skills.")
    if "internship" not in lower_text:
        suggestions.append("Add internship experience if available.")
    if "project" not in lower_text:
        suggestions.append("Mention key academic or personal projects.")

    # Match to careers
    matched_careers = match_careers_from_skills(skills)

    return {
        "skills": list(skills),
        "career_matches": matched_careers,
        "suggestions": suggestions
    }
