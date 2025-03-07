Student Management System

Features

Add, edit, delete, and list students

Search, filter, and sort student records

Django Admin panel for student management

Setup and Installation

1. Clone the repository

git clone YOUR_REPO_URL
cd project2

2. Create and activate virtual environment

python -m venv myenv
source myenv/bin/activate  # Windows: myenv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Configure MySQL Database

Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample2_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Apply migrations

python manage.py makemigrations app2
python manage.py migrate

6. Create superuser (optional for Django Admin)

python manage.py createsuperuser

7. Run the development server

python manage.py runserver

Visit:

Student List: http://127.0.0.1:8000/students/

Django Admin: http://127.0.0.1:8000/admin/

CRUD Operations

List Students: View all students

Add Student: Fill the form and submit

Edit Student: Modify student details

Delete Student: Confirm deletion

GitHub Submission

echo "venv/\n__pycache__/\ndb.sqlite3" >> .gitignore
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main



