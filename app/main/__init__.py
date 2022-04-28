from flask import Blueprint, render_template, request
from app.forms import SignUp, SignIn

main = Blueprint('main', __name__)

@main.route('/', methods = ['GET', 'POST'])
def index():
    signin_form = SignIn()
    return render_template('index.html', signin_form = signin_form)

