from flask import Flask, abort, redirect, render_template, request
from models import db, User
from user_repository import user_repo_singleton

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:password@localhost:5432/name'

db.init_app(app)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/about')
def about():
    return render_template('about.html')

@app.get('/clubs')
def clubs():
    return render_template('clubs.html')

@app.get('/contact')
def contact():
    return render_template('contact.html')

@app.get('/events')
def events():
    return render_template('events.html')

@app.get('/signup')
def signup():
    return render_template('signup.html')

app.post('/signup')
def signup():
    email = request.form.get('signup-email')
    name = request.form.get('signup-name')
    password = request.form.get('signup-password')
    confirm = request.form.get('signup-confirm')

    if(password == confirm):
        new_user = user_repo_singleton.create_user(name, password, email)
        return render_template('clubs.html')
    else:
        return render_template('signup.html')