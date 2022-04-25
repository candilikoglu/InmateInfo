from flask import Blueprint, render_template, request, flash
from website import databaseFunctions

auth = Blueprint('auth', __name__)

JAILOR = 'Jailor'
GUARD = 'Guard'
ADMIN = 'Admin'

@auth.route('/')
@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login_information = (
            request.form.get('Username'),
            request.form.get('Password')
        )
        if len(request.form['Username']) <= 0:
            flash('Please enter username', category='error')
        elif len(request.form['Password']) <=0:
            flash('Please enter password', category='error')
        elif databaseFunctions.check_if_user_exists(JAILOR, login_information[0], login_information[1]):        
            return render_template('home.html', occupation=JAILOR)
        elif databaseFunctions.check_if_user_exists(GUARD, login_information[0], login_information[1]):
            return render_template('home.html', occupation=GUARD)
        elif databaseFunctions.check_if_user_exists(ADMIN, login_information[0], login_information[1]):
            return render_template('home.html', occupation= ADMIN)
        else:
            flash('Login information is incorrect', category='error')
    
    return render_template('login.html')

@auth.route('/logout')
def logout():
    if 'occupation' in databaseFunctions.navbardict:
        del databaseFunctions.navbardict['occupation']
    return render_template('login.html')
