import mysql.connector as c

con = c.connect(host='localhost',
                user='root',
                passwd='Ashish12@',
                database='bankmanagement')
cursor = con.cursor()

name = input("ENTER YOUR NAME  ")
age = int(input("ENTER YOUR AGE  "))
id = int(input("ENTER YOUR ID NUMBER  "))
mobile = int(input("ENTER YOUR MOBILE NUMBER  "))
address = input("ENTER YOUR ADDRESS  ")

query = "insert into account values ('{}',{},{},{},'{}')".format(name, age, id, mobile, address)

cursor.execute(query)
con.commit()
print("DATA ENTER SUCCESSFULLY  ")
