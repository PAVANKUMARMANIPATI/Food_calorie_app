# Food Calorie App

A Django-based application for tracking food calories.

## Deployment to Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following environment variables:
   - `DEBUG=False`
   - `SECRET_KEY` (generate a secure secret key)
   - `ALLOWED_HOSTS=your-render-domain`
   - `DATABASE_URL` (if using PostgreSQL)

4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn calorie_app.wsgi:application`

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file with your local settings
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
