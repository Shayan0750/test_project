# AI News Portal 📰🤖

A simple news article website built with Django.  
Users can sign up, write articles, comment, like, and manage their profile.

## Features

- 📰 View all news articles
- ✍️ Logged-in users can write, edit, and delete their own articles
- ❤️ Like articles
- 💬 Comment on articles
- 👤 Edit user profile (bio and avatar)
- 🗂️ Browse articles by category
- 🔐 Login / Signup system

## Tech Stack

- Python 3
- Django 5
- SQLite (default)
- HTML, CSS, JavaScript (with AJAX for dynamic loading)

## How to Run

```bash
git clone https://github.com/Shayan0750/django-news-site.git
cd django-news-site
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
