import sqlite3


def setDatabaseConnection():
    try:
        con = sqlite3.connect(r'Python\SQlite-DB\patient_db.db')
        return con
    except Exception as err:
        print(err)


def getIDs():
    ret = set()
    con = setDatabaseConnection()
    pData = con.execute('select * from PatientData')
    for data in pData:
        ret.add(data[1])
    print(ret)
    return ret


pID_list = getIDs()


class Patient:
    con = setDatabaseConnection()

    def __init__(self, pId, pName, pAge, pAddress, pMobile, pStatus):
        if pId in pID_list:
            print('\nERROR, Patient with this ID already exists!!')
            return
        self.id = pId
        self.name = pName
        self.age = pAge
        self.address = pAddress
        self.mobile = pMobile
        self.status = pStatus
        self.insertData()

    def insertData(self):
        statement = f'insert into PatientData values ("{self.name}", {self.id}, {self.age}, "{self.address}", "{self.mobile}", "{self.status}")'
        self.con.execute(statement)
        self.con.commit()


def menu():
    print('\n\tMENU')
    print('1. see existing patients')
    print('2. add new patient')
    print('3. update patient data')
    print('4. delete a patient')
    print('5. Exit program')
    print('\nYour choice: ')

    choice = int(input())
    return choice


def replaceData(id, name, age, address, mobile, status):
    con = setDatabaseConnection()
    con.execute(f'delete from PatientData where pID={id}')
    con.commit()
    pID_list.remove(id)
    p = Patient(id, name, age, address, mobile, status)


if __name__ == '__main__':
    run = True
    con = setDatabaseConnection()

    while run:
        choice = menu()
        
        if choice == 1:
            pData = con.execute('select * from PatientData')
            for data in pData:
                print(data)

        elif choice == 2:
            print('\nEnter patient details:')
            print('ID: ', end="")
            id = int(input())
            print('name: ', end="")
            name = input()
            print('age: ', end="")
            age = int(input())
            print('address: ', end="")
            address = input()
            print('mobile: ', end="")
            mobile = input()
            p = Patient(id, name, age, address, mobile, 'Active')

        elif choice == 3:
            print('\nEnter patient id: ')
            id = int(input())
            if id in pID_list:
                print('name: ', end="")
                name = input()
                print('age: ', end="")
                age = int(input())
                print('address: ', end="")
                address = input()
                print('mobile: ', end="")
                mobile = input()
                replaceData(id, name, age, address, mobile, 'Active')
            else:
                print('\nExpected ID in not present')

        elif choice == 4:
            print('Enter patient ID: ', end="")
            id = int(input())
            con.execute(f'update PatientData set pStatus="Inactive" where pID={id}')
            con.commit()

        elif choice == 5:
            print('\nTHANK YOU FOR USING DATABASE')
            break

        else:
            print('\n**Please enter a valid choice!!')