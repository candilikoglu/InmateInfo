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
    connie.close()
    return inmate_info

def query_guard_information():
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('SELECT * FROM Guard')
    guard_info = c.fetchall()
    connie.close()
    return guard_info

def query_FIR_information():
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('''
            SELECT FIR.FIRID, FIR.Name, FIR.Description, FIR.Date,
            FIR.Time, Inmate.InmateID, Inmate.Fullname FROM FIR INNER JOIN
            Inmate ON Inmate.FIRID = FIR.FIRID ORDER BY Inmate.FIRID
            ''')
    FIR = c.fetchall()
    connie.close()
    return FIR

def query_complaint_information():
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('''
            select Cases.CaseID, Cases.PoliceID, Cases.ComplaintID, Cases.Postmortem,
            Police.Fullname, Police.Station, Complaint.Date, Complaint.Time,
            Complaint.Description, Complaint.Place, Complaint.InmateID 
            from Cases inner join Police on Police.PoliceID = Cases.PoliceID
            inner join Complaint on Complaint.ComplaintID = Cases.ComplaintID
            ''')
    Complaint = c.fetchall()
    connie.close()
    return Complaint

def get_FIRID():
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('SELECT FIRID FROM FIR')
    FIRID = c.fetchall()
    connie.close()
    return FIRID

def get_InmateID():
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('SELECT InmateID FROM Inmate')
    InmateID = c.fetchall()
    connie.close()
    return InmateID

def get_GuardID():
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute('SELECT GuardID FROM Guard')
    GuardID = c.fetchall()
    connie.close()
    return GuardID

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
    
def insert_guard(guard_details):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    sql_execute_string = ('''
            INSERT INTO Guard
            (GuardID, Fullname, DOB, Address, Duty, Shift, InmateID, Username, Password)
            VALUES (?,?,?,?,?,?,?,?,?)
            ''')
    c.execute(sql_execute_string, guard_details)
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

def insert_fir(fir_details):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    sql_execute_string = ('''
            INSERT INTO FIR
            (FIRID, Name, Description, Date, Time, InmateID)
            VALUES (?,?,?,?,?,?)
            ''')
    c.execute(sql_execute_string, fir_details)
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
    connie.close()
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
    connie.close()
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
    connie.close()
    return inmate_info

def get_guard_information_with_ID(ID):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute("SELECT * FROM Guard WHERE GuardID="+ID+"")
    inmate_info = c.fetchall()
    connie.close()
    return inmate_info

def update_inmate_information(inmate_info):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute("UPDATE Inmate SET DOB="+inmate_info[1]+", Address="+inmate_info[2]+", Sentence="+inmate_info[3]+", Crime="+inmate_info[4]+", FIRID="+inmate_info[2]+" WHERE InmateID="+inmate_info[0]+"")
    connie.close()

def delete_inmate(ID):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute("DELETE FROM Inmate WHERE InmateID=?",(ID))
    connie.commit()
    connie.close()
    
def delete_guard(ID):
    connie = sqlite3.connect(db_path)
    c = connie.cursor()
    c.execute("DELETE FROM Guard WHERE GuardID="+ID+"")
    connie.commit()
    connie.close()