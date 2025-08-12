

# **Food Calorie App**

A **Python-powered Django web application** for tracking food calories with a clean backend and scalable deployment setup.

## **Deployment to Render**

1. **Create a new Web Service** on [Render](https://render.com)

2. Connect your **GitHub repository**

3. **Set the environment variables**:

   * `DEBUG=False`
   * `SECRET_KEY` *(generate a secure secret key)*
   * `ALLOWED_HOSTS=your-render-domain`
   * `DATABASE_URL` *(if using PostgreSQL)*

4. **Build Command**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Start Command**:

   ```bash
   gunicorn calorie_app.wsgi:application
   ```

---

## **Local Development (Python & Django)**

1. **Clone the repository**
2. Create a **Python virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install **dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. Create a **.env** file with local settings
5. Run **Django migrations**:

   ```bash
   python manage.py migrate
   ```
6. Start the **Django development server**:

   ```bash
   python manage.py runserver
   ```

---

✅ **Key Focus**:

* **Python** is the backbone of the application, handling all backend logic.
* **Django** provides the MVC framework, ORM, and routing for building a robust calorie tracking system.
* Designed for **easy deployment** on Render and smooth local development.


