# Online-Testing-System

An AI-enhanced web-based testing platform built with **Django** that allows users to take mock exams, receive instant feedback, and view detailed performance insights. Designed for educational institutions and individuals preparing for competitive or academic exams.

<img width="1920" height="1078" alt="Welcome to Online Testing System - Google Chrome 05-08-2025 15_57_48" src="https://github.com/user-attachments/assets/17517cc0-4d53-4db1-be62-c101166ce16d" />
<img width="1920" height="1078" alt="Welcome to Online Testing System - Google Chrome 05-08-2025 15_57_56" src="https://github.com/user-attachments/assets/156f6aba-91dd-4df6-aac3-5f6eef66f164" />
<img width="1920" height="1078" alt="Welcome to Online Testing System - Google Chrome 05-08-2025 15_58_08" src="https://github.com/user-attachments/assets/d4e91f65-e84f-4742-ac90-e2d4fe3ad239" />
<img width="1920" height="1078" alt="Welcome to Online Testing System - Google Chrome 05-08-2025 15_59_36" src="https://github.com/user-attachments/assets/d5266e9c-e87f-4eb2-a36e-a37fcb4103f1" />
<img width="1920" height="1078" alt="Welcome to Online Testing System - Google Chrome 05-08-2025 16_00_16" src="https://github.com/user-attachments/assets/d01eece2-beb5-4a85-98da-d77e8398627d" />
<img width="1920" height="1078" alt="Welcome to Online Testing System - Google Chrome 05-08-2025 16_00_46" src="https://github.com/user-attachments/assets/3200eed9-1f77-48ce-a0d6-9015954058ce" />
<img width="1920" height="1078" alt="Welcome to Online Testing System - Google Chrome 05-08-2025 16_00_57" src="https://github.com/user-attachments/assets/a8bd6cb2-7c8e-4c56-8686-49d7f99f733a" />
<img width="1920" height="1078" alt="Welcome to Online Testing System - Google Chrome 05-08-2025 16_01_11" src="https://github.com/user-attachments/assets/2fd82a7c-3b9e-43b4-9659-4ed1be2541a2" />
<img width="1920" height="1078" alt="Welcome to Online Testing System - Google Chrome 05-08-2025 16_01_23" src="https://github.com/user-attachments/assets/25867b56-ce5a-4926-b92b-7e292c3db91c" />

---

## 📌 Features

- ✅ User authentication with role-based access (Admin, Candidate)
- 📄 Test creation with custom questions and categories
- 🧠 **AI-powered performance insights** and feedback reports
- 📈 Admin dashboard for results, trends, and user engagement analytics
- ⏱️ Timer-enabled test environment with auto-submit
- 💬 Personalized feedback based on strengths and weaknesses
- 📊 Visual score and question-level performance summaries
- 🗃️ Question bank management with topic-wise filtering
- 🌐 Deployed serverless via Vercel with ASGI + Mangum

---

## 🔧 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Django** | Web backend framework |
| **HTML, CSS** | Frontend structure and styling |
| **Mangum + ASGI** | Serverless API handling on Vercel |
| **SQLite / PostgreSQL** | Development / production databases |
| **Vercel** | Hosting and deployment |
| **Python** | Core backend language |

---

## 📸 Screenshots

| Candidate Test Interface | Admin Dashboard |
|--------------------------|-----------------|
| ![Test UI](./screenshots/test_ui.png) | ![Admin Panel](./screenshots/admin_panel.png) |

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Arpitverma2006/OnlineTestingSystem.git
   cd OnlineTestingSystem
Create Virtual Environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install Requirements

bash
Copy
Edit
pip install -r requirements.txt
Run Migrations & Start Server

bash
Copy
Edit
python manage.py migrate
python manage.py runserver
Login

Visit http://127.0.0.1:8000/

Default credentials (or create via admin panel)

🚀 Deployment on Vercel (ASGI + Mangum)
api/index.py: Entry point for Vercel's serverless ASGI integration

vercel.json: Custom route configuration

runtime.txt: Enforces compatible Python version (3.10 / 3.11)

To deploy:

bash
Copy
Edit
git push origin main
Then connect the repo to Vercel and deploy.

🧠 AI-Driven Insights
Analyzes candidate answers to highlight weak topics

Generates smart suggestions for revision

Tracks user dropout causes and improves re-engagement

📂 Project Structure
php
Copy
Edit
OnlineTestingSystem/
├── api/                # ASGI handler for Vercel (index.py)
├── OnlineTestingSystem/
│   ├── settings.py
│   ├── asgi.py
│   └── ...
├── templates/
├── static/
├── vercel.json
├── runtime.txt
├── requirements.txt
└── manage.py
👨‍💻 Author
Ajay Verma

🧠 Passionate about AI, Python & Full Stack Development

🌐 LinkedIn | GitHub

⭐️ Show Your Support
If you like this project, please consider:

⭐️ Starring the repo

🍴 Forking it to contribute

🗣️ Sharing it with friends preparing for exams

📜 License
This project is licensed under the MIT License.

markdown
Copy
Edit

---

### ✅ To Finish:

- Replace placeholder links for **Live Demo**, **Documentation**, **LinkedIn**, etc.
- Add real screenshots to a `/screenshots` folder for the GitHub preview
- Confirm your `runtime.txt` and `requirements.txt` are correct and present
