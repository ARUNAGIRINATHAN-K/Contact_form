import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for form submissions
class ContactFormSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Route for displaying the contact form and handling submission
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save to the database
        new_submission = ContactFormSubmission(name=name, email=email, message=message)
        db.session.add(new_submission)
        db.session.commit()

        return redirect(url_for('success'))

    return render_template('index.html')

# Route for success page
@app.route('/success')
def success():
    return "Thank you for your submission!"

if __name__ == "__main__":
    # Ensure db.create_all() is called within the application context
    with app.app_context():
        db.create_all()
    app.run(debug=True)
