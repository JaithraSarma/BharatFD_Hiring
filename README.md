# FAQ Project

This project provides a FAQ system with multilingual support, including Hindi and Bengali translations. The system uses Django and DRF to handle the backend, with Google Translate for automatic translation of the questions and answers.

## Table of Contents
+ Installation 
+ API Usage
+ Contribution
+ License

## Prerequisites
- Python 3.12 or later
- Django 5.1.5
- SQLite

## Installation
Follow the steps provided below

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd <project-directory>
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set up the database
- Database chosen can be managed in `settings.py`
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Super User
```bash
python manage.py createsuperuser
```

### Step 5: Run the server
```bash
python manage.py runserver
```

## Working
Access the stored FAQ's and create new one's in the admin panel at `http://127.0.0.1:8000/faqs/?format=json` and `http://127.0.0.1:8000/admin/` respectively.

## Contributions 
We welcome contributions to carry forward and scale up this plain FAQ system.

## License
Project is licensed under the MIT License.
