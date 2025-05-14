# Contact Form Project

## Project Overview

The **Contact Form Project** is a Flask-based web application designed to collect user information through a contact form. The application ensures user input is validated and provides a responsive user interface. Submitted data is stored in an SQLite database, and users are redirected to a success page with a thank-you message upon form submission.

This project is ideal for anyone looking to learn or implement a simple yet functional contact form using Flask, SQLite, and modern web design principles.

---

## Features

- **Flask Web Application**: Backend powered by Flask to handle form submissions and routing.
- **Input Validation**: Ensures fields are not empty, email format is correct, and the message does not exceed 500 characters.
- **Database Integration**: Stores form submissions in an SQLite database.
- **Responsive UI**: Built using **Tailwind CSS** for a mobile-friendly and modern design.
- **Dynamic Form Validation**: Custom JavaScript for real-time validation feedback.
- **Success Page**: Displays a thank-you message after successful form submission.

---

## Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/contact-form-project.git
   cd contact-form-project
   ```

2. **Set Up a Virtual Environment** (Optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   Run the following commands to create the SQLite database and initialize the required tables:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. **Run the Application**:
   ```bash
   flask run
   ```
   The application will be available at `http://127.0.0.1:5000`.

---

## Usage

1. Navigate to the application's home page (`http://127.0.0.1:5000`) to access the contact form.
2. Fill in the required fields:
   - Name
   - Email
   - Message (maximum 500 characters)
3. Submit the form.
4. Upon successful submission:
   - The data will be stored in the SQLite database.
   - You will be redirected to a success page displaying a thank-you message.

---

## Folder Structure

```
contact-form-project/
├── app/
│   ├── templates/        # HTML templates (e.g., base.html, contact_form.html, success.html)
│   ├── static/
│   │   ├── css/          # Tailwind CSS files
│   │   ├── js/           # Custom JavaScript for form validation
│   ├── __init__.py       # Flask application factory
│   ├── forms.py          # Form validation logic
│   ├── models.py         # Database models
│   ├── routes.py         # Application routes
├── migrations/           # Database migration files
├── requirements.txt      # Python dependencies
├── config.py             # Configuration settings for Flask and SQLite
├── run.py                # Entry point to start the Flask application
├── README.md             # Project documentation
```

---

## Dependencies

- **Flask**: Lightweight WSGI web application framework.
- **Flask-WTF**: For form handling and validation.
- **Flask-Migrate**: For database migrations.
- **SQLite**: Lightweight database for storing form submissions.
- **Tailwind CSS**: For responsive UI design.
- **JavaScript**: For dynamic client-side validation.

Install all dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## License Information

This project is licensed under the MIT License. You are free to use, modify, and distribute this project. See the `LICENSE` file for more details.

---

### Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request with your enhancements.

### Author

**Your Name**  
[GitHub Profile](https://github.com/ARUNAGIRINATHAN_K)
