# SocialNet

A basic social media web application built with Django and PostgreSQL, featuring user authentication, post creation with images, likes, comments, and access control.

## 🔥 Features

- User registration, login, logout
- Post creation with text and images
- Like and comment on posts
- User profile editing
- Full access control (only logged-in users can access the app)
- Permissions: only content owners can edit/delete their content

## 🧪 Tech Stack

- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS
- **Authentication**: Django built-in auth system

## Installation

```bash
# 1. Clone & enter project
git clone https://github.com/aref0101/Social-network.git
cd Social-network

# 2. Create & activate virtualenv
# macOS/Linux:
python3 -m venv venv
source venv/bin/activate
# Windows (PowerShell):
python -m venv venv
venv\Scripts\Activate.ps1
# Windows (cmd.exe):
venv\Scripts\activate.bat

# 3. Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. PostgreSQL setup (run these in psql or a DB GUI; replace <db_name>, <db_user>, <password>):
# CREATE DATABASE <db_name>;
# CREATE USER <db_user> WITH PASSWORD '<password>';
# GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <db_user>;

# 5. Create a .env file for sensitive settings (replace placeholders):
cat > .env <<EOF
SECRET_KEY=<your-django-secret-key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://<db_user>:<password>@localhost:5432/<db_name>
EOF

# 6. Apply migrations & (optionally) create superuser
python manage.py migrate
python manage.py createsuperuser

# 7. Run the dev server
python manage.py runserver

# 8. Browse to http://127.0.0.1:8000/
