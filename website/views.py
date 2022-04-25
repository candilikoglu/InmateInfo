from flask import Blueprint, render_template, request, flash
import sqlite3
import os.path
from website import databaseFunctions

views = Blueprint('views', __name__)

# this function will run whenever we go to '/'
@views.route('/home')
def home():
    occupation = databaseFunctions.navbardict['occupation'] 
    return render_template('home.html', occupation = occupation)


@views.route('/inmate', methods=['POST', 'GET'])
def goToInmate():
    inmate_info = databaseFunctions.query_inmate_information()
    occupation = databaseFunctions.navbardict['occupation']
    return render_template('inmate.html', inmate_info = inmate_info, occupation=occupation)


@views.route('/addInmate', methods=['POST', 'GET'])
def addInmate():
    FIRID = databaseFunctions.get_FIRID()
    if request.method == 'GET':
        occupation = databaseFunctions.navbardict['occupation']
        return render_template('addInmate.html', FIRID = FIRID, occupation = occupation)
    
    elif  request.method == 'POST':
        occupation = databaseFunctions.navbardict['occupation']
        inmate_details = (
            request.form.get('InmateID'),
            request.form.get('Fullname'),
            request.form.get('DOB'),
            request.form.get('Address'),
            request.form.get('Sentence'),
            request.form.get('Crime'),
            request.form.get('FIR')
        )
        
        if len(inmate_details[0]) <= 0:
            flash('Inmate ID can not be empty', category='error')
        elif databaseFunctions.check_if_ID_exists(inmate_details[0], 'Inmate', 'InmateID'):
            flash('Inmate ID already exists',category='error')
        elif len(inmate_details[1]) <= 0:
            flash('Fullname can not be empty',category='error')
        elif len(inmate_details[4]) <= 0:
            flash('Sentence can not be empty', category='error')
        elif len(inmate_details[5]) <= 0:
            flash('Crime can not be empty', category='error')
        else:
            flash('Inmate has been added successfully',category='success')
            databaseFunctions.insert_inmate(inmate_details)
            inmate_info = databaseFunctions.query_inmate_information()
            return render_template('inmate.html', inmate_info = inmate_info, occupation = occupation)
        
    return render_template('addInmate.html', FIRID = FIRID, occupation = occupation)

@views.route('/addJailor', methods=['POST', 'GET'])
def addJailor():
    
    FIRID = databaseFunctions.get_FIRID()
    InmateID = databaseFunctions.get_InmateID()
    
    if request.method == 'GET':
        occupation = databaseFunctions.navbardict['occupation']
        return render_template('addJailor.html', FIRID = FIRID, InmateID = InmateID, occupation = occupation)
    
    if request.method == 'POST':
        newjailor_information = (
            request.form.get('JailorID'),
            request.form.get('Fullname'),
            request.form.get('Address'),
            request.form.get('Shift'),
            request.form.get('Inmates'),
            request.form.get('FIR'),
            request.form.get('Username'),
            request.form.get('password1'),            
        )       
        
        password2  = request.form['password2']
        
        if  len(newjailor_information[0]) <= 0:
            flash('Jailor ID can not be empty', category='error')
        elif databaseFunctions.check_if_ID_exists(newjailor_information[0], 'Jailor', 'JailorID'):
            flash('A jailor with this ID already exists', category='error')
        elif len(newjailor_information[1]) <=0:
            flash('Fullname can not be empty', category='error')
        elif len(newjailor_information[6]) <= 0:
            flash('Username can not be empty', category='error')
        elif len(newjailor_information[7]) <= 0:
            flash('Password can not be empty', category='error')
        elif newjailor_information[7] != password2:
            flash('Passwords do not match', category='error')
        else:
            flash('Jailor has been added successfully',category='success')
            databaseFunctions.insert_jailor(newjailor_information)
            
        
    occupation = databaseFunctions.navbardict['occupation']       
    return render_template('addJailor.html', occupation=occupation)

@views.route('/updateInmate/<int:inmate_id>', methods=['POST', 'GET'])
def updateInmate(inmate_id):
    FIRID = databaseFunctions.get_FIRID()
    inmate_info = databaseFunctions.get_inmate_information_with_ID(str(inmate_id))
    occupation = databaseFunctions.navbardict['occupation']
    
    if request.method == 'GET':
        return render_template('updateInmate.html', inmate_info = inmate_info, FIRID=FIRID)
    else:
        inmate_details = (
            request.form.get('InmateID'),
            request.form.get('Fullname'),
            request.form.get('DOB'),
            request.form.get('Address'),
            request.form.get('Sentence'),
            request.form.get('Crime'),
            request.form.get('FIR')
        )
        
        if len(inmate_details[3]) <= 0:
            flash('Sentence can not be empty', category='error')
        elif len(inmate_details[4]) <= 0:
            flash('Crime can not be empty', category='error')
        else:
            flash('Inmate Information has been successfully changed',category='success')
            databaseFunctions.delete_inmate(str(inmate_id))
            databaseFunctions.insert_inmate(inmate_details)
            inmate_info = databaseFunctions.query_inmate_information()
            return render_template('inmate.html', inmate_info = inmate_info, occupation = occupation)
        

    