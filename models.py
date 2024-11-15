from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    def __init__(self, name, login, password, email, phone):
        self.name = name
        self.login = login
        self.password = password
        self.email = email
        self.phone = phone

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('Users', backref=db.backref('skills', lazy=True))
    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    institution_name = db.Column(db.String(25), nullable=False)
    degree = db.Column(db.String(30), nullable=False)
    date_start = db.Column(db.Date, nullable=False)
    date_end = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('Users', backref=db.backref('education', lazy=True))
    def __init__(self, institution_name, degree, date_start, date_end, user_id):
        self.institution_name = institution_name
        self.degree = degree
        self.date_start = date_start
        self.date_end = date_end
        self.user_id = user_id

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_title = db.Column(db.String(25), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('Users', backref=db.backref('projects', lazy=True))
    def __init__(self, project_title, description, url, user_id):
        self.project_title = project_title
        self.description = description
        self.url = url
        self.user_id = user_id

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume_title = db.Column(db.String(100), nullable=False)
    resume_body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('Users', backref=db.backref('resumes', lazy=True))
    def __init__(self, resume_title, resume_body, user_id):
        self.resume_title = resume_title
        self.resume_body = resume_body
        self.user_id = user_id

with app.app_context():
    db.create_all()
    new_user = Users('Dave', 'IS', 'P@ssw0rd', 'sgsggs@hdhs.com', '5454545454545')
    db.session.add(new_user)
    db.session.commit()
