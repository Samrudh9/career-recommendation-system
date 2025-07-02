import pandas as pd

data = [
    {
        "Skills": "Python, SQL",
        "Career": "Data Scientist",
        "Entry_level_salary": "700000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Java, Android",
        "Career": "Mobile App Developer",
        "Entry_level_salary": "500000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Communication, Leadership",
        "Career": "Project Manager",
        "Entry_level_salary": "600000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "HTML, CSS, JavaScript",
        "Career": "Frontend Developer",
        "Entry_level_salary": "450000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "C++, Algorithms",
        "Career": "Software Engineer",
        "Entry_level_salary": "500000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "R, Statistics",
        "Career": "Statistician",
        "Entry_level_salary": "400000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Python, TensorFlow",
        "Career": "Machine Learning Engineer",
        "Entry_level_salary": "425000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Cybersecurity, Networking",
        "Career": "Cybersecurity Analyst",
        "Entry_level_salary": "450000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Linux, Shell Scripting",
        "Career": "System Administrator",
        "Entry_level_salary": "475000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Adobe Photoshop, Illustrator",
        "Career": "Graphic Designer",
        "Entry_level_salary": "500000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "3D Modeling, CAD",
        "Career": "CAD Designer",
        "Entry_level_salary": "400000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Excel, Business Analysis",
        "Career": "Business Analyst",
        "Entry_level_salary": "425000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Python, Flask",
        "Career": "Backend Developer",
        "Entry_level_salary": "450000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Salesforce, CRM",
        "Career": "CRM Specialist",
        "Entry_level_salary": "475000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "SEO, Google Analytics",
        "Career": "Digital Marketer",
        "Entry_level_salary": "500000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Python, Pandas, Numpy",
        "Career": "Data Analyst",
        "Entry_level_salary": "400000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "MATLAB, Control Systems",
        "Career": "Control Systems Engineer",
        "Entry_level_salary": "425000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "SAP, ERP Systems",
        "Career": "SAP Consultant",
        "Entry_level_salary": "450000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Python, Pytorch",
        "Career": "AI Researcher",
        "Entry_level_salary": "475000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "AWS, Docker, Kubernetes",
        "Career": "DevOps Engineer",
        "Entry_level_salary": "500000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Financial Modeling, Excel",
        "Career": "Financial Analyst",
        "Entry_level_salary": "400000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "English, Storytelling",
        "Career": "Content Writer",
        "Entry_level_salary": "425000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Recruitment, Onboarding",
        "Career": "HR Manager",
        "Entry_level_salary": "450000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Excel, Taxation",
        "Career": "Accountant",
        "Entry_level_salary": "475000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Teaching, Mentoring",
        "Career": "Educator",
        "Entry_level_salary": "500000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Event Planning, Budgeting",
        "Career": "Event Manager",
        "Entry_level_salary": "400000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Negotiation, Market Research",
        "Career": "Sales Executive",
        "Entry_level_salary": "425000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Research, Writing",
        "Career": "Journalist",
        "Entry_level_salary": "450000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "UI/UX Design, Figma",
        "Career": "UX Designer",
        "Entry_level_salary": "475000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    },
    {
        "Skills": "Java, Spring Boot",
        "Career": "Full Stack Developer",
        "Entry_level_salary": "500000",
        "Qualification_required": "B.Tech,Bsc,BCA"
    }
]

df = pd.DataFrame(data)
df.to_csv("dataset/career_data_with_qualifications.csv", index=False)

print("career_data_with_qualifications.csv created successfully with 30 careers and qualification requirements.")
