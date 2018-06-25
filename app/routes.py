from app import app
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'abdalrahman'}
    posts = [
        {'author': {'username':'abd1'},
         'body':'alright, alright, alright!'},
        {'author':{'username':'Susan'},
         'body':'The Avengers movie was cool'}
    ]
    return render_template('index.html', title=None, user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is none or not user.check_passowrd(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember= form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)
