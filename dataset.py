import pandas as pd

data = [
    {
        "Skills": "Python, SQL",
        "Interests": "Data Analysis, Problem Solving",
        "Career": "Data Scientist",
        "Description": "A professional who uses data to generate insights and build predictive models to help decision-making."
    },
    {
        "Skills": "Java, Android",
        "Interests": "App Development, UI Design",
        "Career": "Mobile App Developer",
        "Description": "Specializes in creating applications for mobile devices using platforms like Android or iOS."
    },
    {
        "Skills": "Communication, Leadership",
        "Interests": "Teamwork, Public Speaking",
        "Career": "Project Manager",
        "Description": "Oversees project planning and execution while leading teams to achieve goals efficiently."
    },
    {
        "Skills": "HTML, CSS, JavaScript",
        "Interests": "Web Design, UX",
        "Career": "Frontend Developer",
        "Description": "Builds interactive and responsive user interfaces for websites and web applications."
    },
    {
        "Skills": "C++, Algorithms",
        "Interests": "Competitive Programming, Logic Building",
        "Career": "Software Engineer",
        "Description": "Designs, develops, and maintains software systems and applications."
    },
    {
        "Skills": "R, Statistics",
        "Interests": "Data Visualization, Research",
        "Career": "Statistician",
        "Description": "Uses statistical methods to collect and analyze data for research and decision-making."
    },
    {
        "Skills": "Python, TensorFlow",
        "Interests": "AI, Neural Networks",
        "Career": "Machine Learning Engineer",
        "Description": "Develops algorithms that allow computers to learn from data and improve over time."
    },
    {
        "Skills": "Cybersecurity, Networking",
        "Interests": "Security Systems, Hacking Prevention",
        "Career": "Cybersecurity Analyst",
        "Description": "Protects systems and networks from cyber threats and unauthorized access."
    },
    {
        "Skills": "Linux, Shell Scripting",
        "Interests": "System Administration, Server Management",
        "Career": "System Administrator",
        "Description": "Maintains and configures servers, networks, and IT infrastructure."
    },
    {
        "Skills": "Adobe Photoshop, Illustrator",
        "Interests": "Graphic Design, Branding",
        "Career": "Graphic Designer",
        "Description": "Creates visual content to communicate messages and enhance branding."
    },
    {
        "Skills": "3D Modeling, CAD",
        "Interests": "Architecture, Product Design",
        "Career": "CAD Designer",
        "Description": "Designs and models 2D/3D structures and components using specialized software."
    },
    {
        "Skills": "Excel, Business Analysis",
        "Interests": "Market Trends, Reporting",
        "Career": "Business Analyst",
        "Description": "Bridges the gap between business needs and technology solutions through data analysis."
    },
    {
        "Skills": "Python, Flask",
        "Interests": "Web Apps, APIs",
        "Career": "Backend Developer",
        "Description": "Develops the logic, database interaction, and server-side functionality of web apps."
    },
    {
        "Skills": "Salesforce, CRM",
        "Interests": "Customer Relations, Automation",
        "Career": "CRM Specialist",
        "Description": "Manages customer relationships using CRM software to enhance sales and marketing efforts."
    },
    {
        "Skills": "SEO, Google Analytics",
        "Interests": "Marketing, Content Optimization",
        "Career": "Digital Marketer",
        "Description": "Promotes products and services using digital channels and analytics."
    },
    {
        "Skills": "Python, Pandas, Numpy",
        "Interests": "Big Data, Data Cleaning",
        "Career": "Data Analyst",
        "Description": "Analyzes structured data to find trends and support business decisions."
    },
    {
        "Skills": "MATLAB, Control Systems",
        "Interests": "Robotics, Automation",
        "Career": "Control Systems Engineer",
        "Description": "Designs systems that control dynamic processes in machines and vehicles."
    },
    {
        "Skills": "SAP, ERP Systems",
        "Interests": "Resource Planning, Business Integration",
        "Career": "SAP Consultant",
        "Description": "Implements and manages SAP solutions to streamline enterprise operations."
    },
    {
        "Skills": "Python, Pytorch",
        "Interests": "Deep Learning, Computer Vision",
        "Career": "AI Researcher",
        "Description": "Explores and develops innovative AI technologies and applications."
    },
    {
        "Skills": "AWS, Docker, Kubernetes",
        "Interests": "Cloud Infrastructure, DevOps",
        "Career": "DevOps Engineer",
        "Description": "Manages deployment pipelines and cloud infrastructure for faster development."
    },
    {
        "Skills": "Financial Modeling, Excel",
        "Interests": "Investing, Forecasting",
        "Career": "Financial Analyst",
        "Description": "Analyzes financial data and builds models for budgeting, investing, and forecasting."
    },
    {
        "Skills": "English, Storytelling",
        "Interests": "Writing, Editing",
        "Career": "Content Writer",
        "Description": "Creates written content for blogs, articles, websites, and marketing."
    },
    {
        "Skills": "Recruitment, Onboarding",
        "Interests": "People Management, Policies",
        "Career": "HR Manager",
        "Description": "Manages hiring processes and employee well-being in organizations."
    },
    {
        "Skills": "Excel, Taxation",
        "Interests": "Finance, Law",
        "Career": "Accountant",
        "Description": "Prepares financial records, budgets, and ensures tax compliance."
    },
    {
        "Skills": "Teaching, Mentoring",
        "Interests": "Education, Learning",
        "Career": "Educator",
        "Description": "Facilitates learning and development for students or professionals."
    },
    {
        "Skills": "Event Planning, Budgeting",
        "Interests": "Logistics, Coordination",
        "Career": "Event Manager",
        "Description": "Plans and organizes events ensuring seamless execution."
    },
    {
        "Skills": "Negotiation, Market Research",
        "Interests": "Customer Interaction, Retail",
        "Career": "Sales Executive",
        "Description": "Drives product sales through relationship-building and marketing strategies."
    },
    {
        "Skills": "Research, Writing",
        "Interests": "Journalism, Investigative Reporting",
        "Career": "Journalist",
        "Description": "Reports on current events and topics through writing, interviews, and investigation."
    },
    {
        "Skills": "UI/UX Design, Figma",
        "Interests": "Design Thinking, User Experience",
        "Career": "UX Designer",
        "Description": "Designs user-centric digital products ensuring usability and satisfaction."
    },
    {
        "Skills": "Java, Spring Boot",
        "Interests": "APIs, Server-side Development",
        "Career": "Full Stack Developer",
        "Description": "Works on both frontend and backend development of web applications."
    }
]

df = pd.DataFrame(data)
df.to_csv("dataset/career_data.csv", index=False)

print("career_data.csv with 30 career entries created successfully.")