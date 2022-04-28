from flask import Blueprint, request, session, redirect, url_for, render_template
from app.forms import SignUp, SignIn
from app.models import db, User, Character

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignUp(request.form)
    if request.method == 'POST':
        register_user_data = User(signup_form.username.data, signup_form.password.data)
        db.session.add(register_user_data)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('signup.html', signup_form = signup_form)



@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    signin_form = SignIn()
    if request.method = 'POST':
        username = signin_form.username.data
        # Find the username in the database and pulls up the data for it.
        login = User.query.filter_by(username = username).first()
        #Check the form passowrd against the db password
        if login.password == signin_form.password.data:
            current_user = login.username
            session['current_user'] = current_user
            # Sets the user as logged in as a session variable.  Can check against it
            # to make sure people aren't getting into the wrong place.
            session['user_available'] = True
            return redirect(url_for('character'))
    return render_template('/', signin_form = signin_form)
