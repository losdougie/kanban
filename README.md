# kanban
Simple Kanban based on Django

To install:
1. Clone to a folder: git clone https://github.com/losdougie/kanban
2. Create a virtual environment within the cloned folder: python3 -m venv venv
3. Activate the virtual environment: venv\Scripts\activate.bat -or- source venv/bin/activate
4. Update pip: python -m pip install --upgrade pip
5. Install django: python -m pip install django
6. Change directory to todo and make migrations: python manage.py makemigrations
7. Migrate: python manage.py migrate
8. Create a superuser: python manage.py createsuperuser
9. Run the server: python manage.py runserver
10. Log in to admin: http://localhost:8000/admin
