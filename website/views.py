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
            request.form['InmateID'],
            request.form['Fullname'],
            request.form['DOB'],
            request.form['Address'],
            request.form['Sentence'],
            request.form['Crime'],
            request.form['FIR']
        )
        
        if len(inmate_details[0]) <= 0:
            flash('Inmate ID can not be empty', category='error')
        elif databaseFunctions.check_if_ID_exists(inmate_details[0], 'Inmate'):
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