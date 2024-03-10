from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User, Contact, Education, Skill, Experience 


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/Alejandro-Malanche', methods=['GET'])
def retrieve_user():
    user = db.session.execute(User.query.filter(User.username == 'Alejandro Malanche')).first()[0]
    contact = db.session.execute(Contact.query.filter(Contact.user_id == user.id)).first()[0]
    education = db.session.execute(Education.query.filter(Education.user_id == user.id)).first()[0]
    skills = db.session.execute(Skill.query.filter(Skill.user_id == user.id)).fetchall()
    experience = db.session.execute(Experience.query.filter(Experience.user_id == user.id)).fetchall()
    return render_template('index.html', user=user, contact=contact, education=education, experience=experience, skills=skills)
