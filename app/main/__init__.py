from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.rout('/')
def index():
    return render_template('index.html')