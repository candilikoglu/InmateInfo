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
            request.form['Username'],
            request.form['Password']
        )
        if len(request.form['Username']) <= 0:
            flash('Please enter username', category='error')
        elif len(request.form['Password']) <=0:
            flash('Please enter password', category='error')
        elif databaseFunctions.check_if_attribute_exists(JAILOR, login_information[0], login_information[1]):        
            return render_template('home.html', occupation=JAILOR)
        elif databaseFunctions.check_if_attribute_exists(GUARD, login_information[0], login_information[1]):
            return render_template('home.html', occupation=GUARD)
        elif databaseFunctions.check_if_attribute_exists(ADMIN, login_information[0], login_information[1]):
            return render_template('home.html', occupation= ADMIN)
        else:
            flash('Login information is incorrect', category='error')
    
    return render_template('login.html')


@auth.route('/logout')
def logout():
    if 'occupation' in databaseFunctions.navbardict:
        del databaseFunctions.navbardict['occupation']
    return render_template('login.html')

@auth.route('/createUser', methods=['POST', 'GET'])
def createUser():
    if request.method == 'POST':
        email = request.form.get('email')
        fullName = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 6:
            flash('Email must be greater than 6 characters', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category = 'error')
        elif len(fullName) < 4:
            flash('Full name must be greater than 4 characters', category = 'error')
        else:
            flash('Account created successfully', category='success')
    
    occupation = databaseFunctions.navbardict['occupation']       
    return render_template('createUser.html', occupation=occupation)