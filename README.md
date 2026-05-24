# Job Application Tracker

A full-stack web app to track your job applications — built with Python, Django, and custom HTML/CSS.

![Dashboard Preview](screenshots/dashboard.png)

## Features

- User authentication — register, login, logout
- Add, edit, and delete job applications
- Track status: Applied → Screening → Interview → Offer → Rejected
- Visual progress pipeline bar on each application card
- Dashboard stats — total applied, interviews, offers, rejections
- Search by company or role name
- Filter by application status
- Notes field for each application
- Fully responsive layout

## Tech Stack

| Layer    | Technology              |
|----------|-------------------------|
| Backend  | Python 3, Django 4      |
| Database | SQLite (Django ORM)     |
| Frontend | HTML5, CSS3 (custom)    |
| Auth     | Django built-in auth    |

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/job-tracker.git
cd job-tracker
```

### 2. Create and activate virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. (Optional) Load demo data

```bash
python seed.py
# Login with: demo / demo1234
```

### 6. Start the server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

## Project Structure

job-tracker/
├── jobtracker/         # Django project settings
├── jobs/               # Main app
│   ├── models.py       # Job model
│   ├── views.py        # All views
│   ├── forms.py        # RegisterForm, JobForm
│   ├── urls.py         # URL routing
│   └── templates/jobs/ # HTML templates
├── seed.py             # Demo data script
├── requirements.txt
└── README.md
