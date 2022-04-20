import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "inmate_database.db")

def query_inmate_information():
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('SELECT * FROM Inmate')
    inmate_info = c.fetchall()
    return inmate_info

def add_inmate_information():
    pass

def get_FIRID():
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('SELECT FIRID FROM FIR')
    FIRID = c.fetchall()
    return FIRID

def insert_inmate(inmate_details):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    sql_execute_string = ('INSERT INTO Inmate (InmateID, Fullname, DOB, Address, Sentence, Crime, FIRID) VALUES (?,?,?,?,?,?,?)')
    c.execute(sql_execute_string, inmate_details)
    connie.commit()
    connie.close()
    
def check_if_ID_exists(ID, table):
    #print(ID)
    #print(table)
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute("SELECT "+ID+" FROM "+table+" WHERE InmateID = "+ID+"")
    result = c.fetchall()
    #print(result)
    if len(result) > 0:
        return True
    else:
        return False