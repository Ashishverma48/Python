import mysql.connector as a

con = a.connect(host='localhost',
                user='root',
                passwd='Ashish12@',
                database='bank')

cursor = con.cursor()
accno = input("ENTER YOUR ACCOUNT NUMBER : ")
ob = int(input("ENTER THE AMOUNT : "))

query = "select ob from account where accno='{}'".format(accno)
cursor.execute(query)
data1 = cursor.fetchone()
total = data1[0] + ob
query1 = "update account set ob = {} where accno = '{}'".format(ob, accno)
d = (total,)
cursor.execute(query1, d)
result = cursor.fetchone()
con.commit()
print("success")
