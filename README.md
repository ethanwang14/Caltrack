# Caltrack - Nutrition Tracking Website

A Django-based web application for tracking daily nutrition with weekly goals and progress visualization.
This application uses as the database SQLite to store user data

## Features

- **User Authentication**: Sign up, login, and logout with email and password
- **Home Dashboard**: View weekly nutrition totals with progress bars
- **Food Tracking**: Add food entries with calories, protein, carbs, and fats
- **History**: View all food entries chronologically
- **Goals Management**: Set and update weekly nutrition goals
- **Week Reset**: Clear all data to start a new week

## Setup Instructions

1. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run Migrations:
   ```bash
   python manage.py migrate
   ```

4. Create Superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

4. Start Development Server:
   ```bash
   python manage.py runserver
   ```

6. Access the Application:
   - Open `http://127.0.0.1:8000/`in your browser


## How to Use

1. **Sign Up**: Create a new account with username and password
2. **Log in**: Log in with your username and password
3. **Set Goals**: Go to the Goals page to set your weekly nutrition targets
4. **Track Food**: Use the Track page to enter food/drink entries
5. **Check Progress**: View your weekly progress on the Home page
6. **View History**: Check all your entries on the History page
7. **Reset Week**: Use the Reset Week button to start fresh


## Technology Used

- Django 5.2.7
- SQLite Database
- HTML/CSS/JavaScript
- Bootstrap
