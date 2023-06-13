import mysql.connector as c

con = c.connect(host='localhost',
                user='root',
                passwd='Ashish12@',
                database='bankmanagement')
cursor = con.cursor()


def open():
    name = input("ENTER YOUR NAME  ")
    age = int(input("ENTER YOUR AGE  "))
    id = int(input("ENTER YOUR ID NUMBER  "))
    mobile = int(input("ENTER YOUR MOBILE NUMBER  "))
    address = input("ENTER YOUR ADDRESS  ")

    query = "insert into account values ('{}',{},{},{},'{}')".format(name, age, id, mobile, address)

    cursor.execute(query)
    con.commit()
    print("DATA ENTER SUCCESSFULLY  ")
    main()

def deposit():








def details():
    query = "select * from account"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    main()

def main():
    print("""
    1. OPEN NEW ACCOUNT 
    2. CASH DEPOSIT 
    3. CASH WITHDRAW
    4. ACC DETAILS 
    5. CLOSE ACCOUNT
    6. EXIT 
    
    SELECT YOUR OPTION (1-6) """)

    choice = input("ENTER YOUR OPTION NUMBER : ")
    if choice == '1':
        open()
    # elif choice=='2':
    #   deposit()
    # elif choice=='3':
    #   withdraw()
    elif choice == '4':
        details()
    # elif choice=='5':
    #   close()
    # elif choice=='6':
    #   exit()

main()
