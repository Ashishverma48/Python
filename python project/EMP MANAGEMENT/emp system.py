import mysql.connector as a

con = a.connect(host='localhost',
                user='root',
                passwd='Ashish12@',
                database='emp')
cursor = con.cursor()
def addemp():

    name = input("ENTER YOUR NAME : ")
    id = input("ENTER YOUR ID NUMBER : ")
    post = input("ENTER YOUR POST : ")
    ph = input("ENTER PHONE NUMBER : ")
    sal = int(input("ENTER YOUR SALARY : "))
    data = (name, id, post, ph, sal)
    query = "insert into emp values (%s,%s,%s,%s,%s)"
    cursor.execute(query, data)
    con.commit()
    print("SUCCESSFULLY ENTER DETAILS ")

def allemp():


    query = "select * from emp"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i)

def empdetails():

    id = input("ENTER EMPLOYEE ID NUMBER  : ")
    query = "select * from emp where id=%s"
    data = (id,)
    cursor.execute(query,data)
    result = cursor.fetchall()
    for i in result:
        print(i)

def remove_emp():

    id = input("ENTER EMP ID NUMBER : ")
    query = "delete from emp where id=%s"
    data =(id,)
    cursor.execute(query,data)
    con.commit()
    print("SUCCESSFULLY REMOVE EMPLOYEE ")

def update():
    print('''
    1. NAME UPDATE
    2. POST UPDATE 
    3. PHONE UPDATE
    4. SALARY UPDATE ''')
    choice = input("ENTER CHOICE NUMBER ")
    if choice == '1':
        id = input("ENTER ID NUMBER  :  : ")
        name = input("UPDATE NAME :   ")
        query = "update emp set name=%s where id = %s"
        data = (name, id)
        cursor.execute(query, data)
        con.commit()
        print("SUCCESFULLY UPDATE")

    elif choice == '2':
        id = input("ENTER THE ID NUMBER :  : ")
        post = input("UPDATE EMP POST  ")
        query = "update emp set post=%s where id = %s"
        data = (post, id)
        cursor.execute(query, data)
        con.commit()
        print("SUCCESSFULLY POST UPDATE ")

    elif choice == '3':
        id = input("ENTER ID NUMBER : ")
        phone = input("UPDATE PHONE NUMBER :   ")
        query = "update emp set ph=%s where id = %s"
        data = (phone, id)
        cursor.execute(query, data)
        con.commit()
        print("SUCCESSFULLY PHONE NUMBER UPDATE ")

    elif choice == '4':
        id = input("ENTER ID NUMBER  : ")
        salary = input("ENTER  NEW SALARY :  ")
        query = "update emp set sal=%s where id = %s"
        data = (salary, id)
        cursor.execute(query, data)
        con.commit()
        print("SUCCESSFULLY SALARY UPDATE ")

    else:
        print("WRONG NUMBER PLEAS SELECT 1-4 ")


def exit():
    print("THANKS FOR USING EMPLOYEE MANAGEMENT SYSTEM ")
    quit()


def main():
    print('''
     1. ADD NEW EPMLOYEE
     2. VIEW ALL EMP
     3. VIEW EMP DETAILS BY ID
     4. REMOVE EMPLOYEE
     5. UPDATE EMPLOYEE DETAILS
     6. EXIT''')

choice = input("ENTER CHOICE NUMBER 1-7  ")
if choice =='1':
    addemp()
elif choice =='2':
    allemp()
elif choice =='3':
    empdetails()
elif choice =='4':
    remove_emp()
elif choice =='5':
    update()
elif choice =='6':
    exit()
else:
    print("")