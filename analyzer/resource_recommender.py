resource_links = {
    "python": "https://www.learnpython.org/",
    "sql": "https://www.w3schools.com/sql/",
    "flask": "https://flask.palletsprojects.com/en/2.3.x/",
    "aws": "https://aws.amazon.com/training/",
    # Add more mappings
}

def recommend_resources(skill_gaps):
    return {skill: resource_links.get(skill, "Search on Google") for skill in skill_gaps}
