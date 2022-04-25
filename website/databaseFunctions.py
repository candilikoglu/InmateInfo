import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "inmate_database.db")

navbardict = {}

def query_inmate_information():
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('SELECT * FROM Inmate')
    inmate_info = c.fetchall()
    return inmate_info

def get_FIRID():
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('SELECT FIRID FROM FIR')
    FIRID = c.fetchall()
    return FIRID

def get_InmateID():
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('SELECT InmateID FROM Inmate')
    InmateID = c.fetchall()
    return InmateID

def insert_inmate(inmate_details):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    sql_execute_string = ('''
            INSERT INTO Inmate
            (InmateID, Fullname, DOB, Address, Sentence, Crime, FIRID)
            VALUES (?,?,?,?,?,?,?)
            ''')
    c.execute(sql_execute_string, inmate_details)
    connie.commit()
    connie.close()
    
def insert_jailor(jailor_details):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    sql_execute_string = ('''
            INSERT INTO Jailor
            (JailorID, Fullname, Address, Shift, InmateID, FIRID, Username, Password)
            VALUES (?,?,?,?,?,?,?,?)
            ''')
    c.execute(sql_execute_string, jailor_details)
    connie.commit()
    connie.close()
    
def check_if_ID_exists(ID, table, column_name):
    #print(ID)
    #print(table)
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('SELECT '+ID+' FROM '+table+' WHERE '+column_name+' = '+ID+'')
    result = c.fetchall()
    # print(result)
    if len(result) > 0:
        return True
    else:
        return False
    
def check_if_user_exists(table, username, password):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute("SELECT * FROM "+table+" WHERE Username=? AND Password=?", (username, password))
    result = c.fetchall()
    #print('THIS IS THE RESULT', result)
    if len(result) > 0:
        navbardict['occupation'] = table
        return True
    else:
        return False
    
def get_inmate_information_with_ID(ID):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute("SELECT * FROM Inmate WHERE InmateID=?", (ID))
    inmate_info = c.fetchall()
    return inmate_info

def update_inmate_information(inmate_info):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute("UPDATE Inmate SET DOB="+inmate_info[1]+", Address="+inmate_info[2]+", Sentence="+inmate_info[3]+", Crime="+inmate_info[4]+", FIRID="+inmate_info[2]+" WHERE InmateID="+inmate_info[0]+"")
    

def delete_inmate(ID):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute("DELETE FROM Inmate WHERE InmateID=?",(ID))
    connie.commit()
    connie.close()