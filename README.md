# Django AI Course Platform 🎓🤖

A Django-based web application that allows users to:

- Browse programming courses
- Register and login to track progress
- Mark courses as completed
- Simple & clean UI with a chatbot integrated using Gemini AI (basic interface)

---

## Features

✅ User Registration & Login  
✅ Search Courses by Title & Category  
✅ Mark Course as Completed  
✅ Responsive Frontend Design  
✅ Gemini AI Chatbot Integrated for Course Suggestions (currently basic functionality)

---

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3 (with inline styles)
- **AI Integration**: Gemini AI API (Google Generative AI)
- **Database**: SQLite3 (for development)
- **Deployment**: Render

---

## Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/django-ai-course-platform.git
cd django-ai-course-platform
2️⃣ Create Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # For Mac/Linux
# OR
.venv\Scripts\activate  # For Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set up Gemini API key
You need to have a Gemini AI API key:

Create a file named .env or set your environment variable:

bash
Copy
Edit
export GEMINI_API_KEY=your_actual_api_key
5️⃣ Apply Migrations
bash
Copy
Edit
python manage.py migrate
6️⃣ Run Development Server
bash
Copy
Edit
python manage.py runserver
Deployment Notes
Render deployment is configured with:

Whitenoise for static file management

SQLite for simplicity (can be upgraded for production)

Environment variable GEMINI_API_KEY must be configured on Render

Screenshots
(You can optionally add screenshots of your app interface here.)

Future Improvements
✅ Stable core app

⬜ AI-powered MCQ quiz generation (optional)

⬜ AI-powered dynamic search suggestions (optional)

⬜ Admin panel for adding more courses

License
This project is for educational/demo purposes.
Feel free to fork, modify, and build on top of it 🚀

Made with ❤️ using Django + Gemini AI.
