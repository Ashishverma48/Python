import mysql.connector

mydatabase = mysql.connector.connect(host='localhost', user='root', password='Ashish12@', database='bank_management')


def openacc():
    name = input("ENTER THE NAME")
    ac = input("ENTER THE ACCOUNT NUMBER")
    dob = input("ENTER THE DATE OF BIRTH ")
    add = input("ENTER THE ADDRESS ")
    con = int(input('ENTER THE ACCOUNT NUMBER'))
    op = int(input("ENTER THE OPENING AMOUNT "))
    data1 = (name, ac, dob, add, con, op)
    data2 = (name, ac, op)
    sql1 = "insert into account values (%s,%s,%s,%s,%s,%s"
    sql2 = "insert inro amount values (%s,%s,%s"
    x = mydatabase.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    print("DATA ENTERED SUCCESFULLY  ")
    main()


def deposit():
    amount = int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT"))
    ac = input("ENTER THE ACCOUNT NUMBER")
    a = "select balance from amount where Acc-no=%s"
    data = (ac,)
    x = mydatabase.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] + amount
    sql = 'update amount set balance where Acc-no=%s'
    d = (t, ac)
    x.execute(sql, d)
    mydatabase.commit()
    main()


def withdraw():
    amount = int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW"))
    ac = input("ENTER THE ACCOUNT NUMBER")
    a = "select balance from amount where Accno=%s"
    data = (ac,)
    x = mydatabase.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = "update balance from amount where Accno=%s"
    d = (t, ac)
    x.execute(sql, d)
    mydatabase.commit()
    main()


def balance():
    ac = input("ENTER THE ACCOUNT NO.  ")
    a = 'select a from amount where Accno=%s'
    data = (ac,)
    x = mydatabase.cursor()
    x.execute(a, data)
    result = x.fetchone()
    print("BALANCE FOR ACCOUNT  ", ac, '  is', result[-1])
    main()


def display():
    ac = input("ENTER THE ACCOUNT NO.  ")
    a = 'select a from account where Accno=%s'
    data = (ac,)
    x = mydatabase.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()


def closeacc():
    ac = input("ENTER THE ACCOUNT NUMBER  ")
    sql1 = 'delete from account where accno=%s'
    sql2 = 'delete from amount where accno=%s'
    data = (ac,)
    x = mydatabase.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    mydatabase.commit()
    main()


def main():
    print('''
    1. OPEN NEW ACCOUNT
    2. DEPOSITE AMOUNT
    3. WITHDRAW AMOUNT
    4. BALANCE INQUARY
    5. DISPLAY COSTUMER DETAILS
    6. CLOSE AN ACCOUNT
    ''')

    choice = input("ENTER THE TASK YOU WANT TO PERFORM  ")
    if choice == '1':
        openacc()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        balance()
    elif choice == '5':
        display()
    elif choice == '6':
        closeacc()
    else:
        print("INVALID CHOICE ")
    main()
