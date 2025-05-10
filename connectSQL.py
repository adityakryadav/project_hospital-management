import json
import pickle
import mysql.connector as mys
from datetime import date

con=mys.connect(
    host="localhost", 
    user="root", 
    passwd="aditya@sql", 
    database="hospital", 
    auth_plugin="mysql_native_password"
    )
cur=con.cursor()


cur.execute("Select * from hospitalData where mail='aiims@gmail.com'")
hData=cur.fetchall()
# for i in hData:
#     print(i[0])
print(hData)             #LIST OF TUPLES

cur.execute("Select * from individualData")
pData=cur.fetchall()
# for i in pData:
#     print(i[0])
print(pData)             #LIST OF TUPLES

cur.execute("Select MAIL from hospitalData")
IDs=cur.fetchall()
print(IDs)

l1 = []
if l1:
    print("Not Empty")
else:
    print("Empty")
hos_id="vhospital@gmail.com"
cur.execute("Select * from hospitalData WHERE MAIL='%s'"%(hos_id,))
dtl=cur.fetchall()
print(dtl)



# Patient Records
cur.execute("SHOW TABLES")
mydb=cur.fetchall()
data = {}

for table in mydb:
    if table[0] != "hospitaldata" and table[0] != "individualdata":
        cur.execute("SELECT * FROM %s WHERE PT_NAME='%s' AND PSWD='%s'"%(table[0], dtl[0][2], dtl[0][1]))
        val=cur.fetchall()
        print
        data[table[0] + "@gmail.com"] = val

print(json.dumps(data,indent=5))