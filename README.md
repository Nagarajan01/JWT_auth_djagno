# JACKPOT
—-----Description------- 

# What do I need first?

Nothing much, just Python 3+ and (ideally) virtualenv.

# How do I start it?

Clone the repo, cd to the repo directory, and run it (ideally inside a virtual environment).

# List the technologies and tools used in the project. Example:
- Python 3.10
- Django 4.1.4
- Djangorestframework 3.14.0
- Django-celery-beat 2.4.0
- PostgreSQL 12 or later


# Installing:
1. Clone the repository: `git clone https://github.com/jayapal/jackpot-backend.git`
2. Navigate to the project directory: `cd jackpot-backend`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment: `source env/bin/activate` (for Linux/Mac) or `env\Scripts\activate.bat` (for Windows)
5. Navigate to the directory: `cd jackpot`
6. Install the dependencies: `pip install -r requirements.txt`
7. Create the tables to database: `python manage.py makemigrations`
8. Apply migration to the database: `python manage.py migrate`
9. Run the development server: `python manage.py runserver`
10. Run a Celery worker with beat scheduler: `celery -A jackpot worker --beat -l info`


# Creating users(Both admin and users):
1. To create an admin user, an admin user can use the terminal or the admin panel to create the user account. After creating the admin user account, the admin can log in to the admin panel and manually create a group for other admin users and add admin users to this group(Group name should me "Admin").

2. To create a regular user, an endpoint like /users/register can be used. Once a new user is registered, the application can automatically create a user group and add the user to that group.





