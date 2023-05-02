import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, abort, redirect, render_template, request
from models import db, User
from user_repository import user_repo_singleton

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:password@localhost:5432/name'

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/clubs')
def clubs():
    return render_template('clubs.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('signup-email')
        name = request.form.get('signup-name')
        password = request.form.get('signup-password')
        confirm = request.form.get('signup-confirm')

        if(password == confirm):
            new_user = user_repo_singleton.create_user(name, password, email)
            return render_template('clubs.html')
        else:
            return render_template('signup.html')
    else:
        return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
