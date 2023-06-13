 # UPDATE DATA
import mysql.connector as a
emp = a.connect(host="localhost",
               user= "root",
               password = "Ashish12@",
               database='emp')
cursor = emp.cursor()
query = """
UPDATE employee
SET NAME='ASHISH KUMAR'
WHERE ID=112
"""
cursor.execute(query)
emp.commit()

cursor.execute("SELECT * FROM employee;")

for i in cursor:
    print(i)