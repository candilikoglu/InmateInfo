from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# this function will run whenever we go to '/'
@views.route('/')
def home():
    # return "<h1>hello</h1>" 
    return render_template('home.html')