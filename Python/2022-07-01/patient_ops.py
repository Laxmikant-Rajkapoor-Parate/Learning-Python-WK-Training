import sqlite3

def set_connection():
    try:
        con = sqlite3.connect(r'Python\SQlite-DB\patient_db.db')
        return con
    except Exception as e:
        print(e)

def get_data(con):
    patient_data = con.execute('Select * from PatientData')
    for data in patient_data:
        print(data)

def update_patient_data(con, pid, age):
    con.execute(f'Update PatientData set pAge={age} where pID={pid}')
    con.commit()

def delete_patient(con, pid):
    status = 'Inactive'
    con.execute(f"Update PatientData set pStatus='{status}' where pID={pid}")
    con.commit()

if __name__ == '__main__':
    con = set_connection()
    update_patient_data(con, 2, 99)
    delete_patient(con, 1)
    get_data(con)
    