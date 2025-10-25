# Caltrack - Nutrition Tracking Website



A Django-based web application for tracking daily nutrition with weekly goals and progress visualization.



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



3. Create Superuser** (optional):

   ```bash

   python manage.py createsuperuser

   ```



4. Start Development Server:

   ```bash

   python manage.py runserver

   ```



5. Access the Application:

   - Open your browser and go to `http://127.0.0.1:8000/`

   - Sign up for a new account or use the admin account (admin/admin123)



## How to Use



1. **Sign Up**: Create a new account with username and password

2. **Set Goals**: Go to the Goals page to set your weekly nutrition targets

3. **Track Food**: Use the Track page to add food entries

4. **Monitor Progress**: View your weekly progress on the Home page

5. **View History**: Check all your entries on the History page

6. **Reset Week**: Use the Reset Week button to start fresh



## Models



- UserProfile: Extended user information

- Goals: Weekly nutrition goals (calories, protein, carbs, fats)

- FoodEntry: Individual food entries with nutrition data



## Features Implemented



User authentication system  

Responsive navigation sidebar  

Weekly totals with progress bars  

Food entry form with validation  

History page with chronological entries  

Goals management  

Week reset functionality  

Modern UI with CSS styling  

Form validation and error handling  



## Default Admin Account



- Username: `admin`

- Password: `admin123`



## Technology Stack



- Django 5.2.7

- SQLite Database

- HTML/CSS/JavaScript

- Bootstrap-inspired styling

