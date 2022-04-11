from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"

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
            
    return render_template('createUser.html')