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


cur.execute("Select * from hospitalData")
hData=cur.fetchall()
# for i in hData:
#     print(i[0])
print(hData)             #LIST OF TUPLES

cur.execute("Select * from individualData")
pData=cur.fetchall()
# for i in pData:
#     print(i[0])
print(pData)             #LIST OF TUPLES


print("\n***************************** WELCOME TO COMBINED NETWORK OF ALL HOSPITALS AND PATIENTS *****************************\n")
earn=0                                          # Renewing Patients For Today as ZERO
rate={'Fever':3000,'Cold':3700,'Food Poisoning':5600}
while True:
    print("---------------------------------------------------------  ------------ For Example [ALREADY REGISTERED] -----------")
    print("| Type:-                                                |  | ID : vhospital@gmail.com            PASS : 123v@      |")
    print("| 1 - If you are entering as a Hospital                 |  | ID : orthohos@gmail.com             PASS : ortho123   |")
    print("| 2 - If you are entering as a Patient                  |  | ID : aditya@gmail.com               PASS : aditya@123 |")
    print("| 5 - to exit from anywhere                             |  | [NOTE : Still you can create your own account.]       |")
    print("---------------------------------------------------------  ---------------------------------------------------------\n")
    ch1=int(input('What you want?\n'))
    if ch1==1:
        while True:
            print("---------------------------------------------------------")
            print("| Type:-                                                |")
            print("| 5 - to exit                                           |")
            print("---------------------------------------------------------\n")
            hos_id=input("Please enter your Login ID : ")

            cur.execute("Select MAIL from hospitalData WHERE MAIL='%s'"%(hos_id,))
            present=cur.fetchall()

            if present:
                while True:
                    print("---------------------------------------------------------")
                    print("| Type:-                                                |")
                    print("| 5 - to exit                                           |")
                    print("---------------------------------------------------------\n")

                    b=input('Please Enter your Password : ')

                    cur.execute("Select * from hospitalData WHERE MAIL='%s'"%(hos_id,))
                    dtl=cur.fetchall()

                    if b==dtl[0][2]:

                        print("\n***********************",dtl[0][3],"***********************\n")
                        while True:
                            print("---------------------------------------------------------")
                            print("| Type:-                                                |")
                            print("| 1 - Want to Check Patient Details                     |")
                            print("| 2 - For Adding Data of Other Patients(Offline)        |")
                            print("| 3 - To Check the Valuation of Your Hospital(Earned)   |")
                            print("| 5 - to exit                                           |")
                            print("---------------------------------------------------------\n")
                            ch2=int(input("Enter Your Choice : "))
                            if ch2==1:
                                n=len(hos_id)                
                                tblName=(hos_id)[:(n-10)]
                                cur.execute("SELECT * FROM %s"%(tblName,))
                                ptRecords = cur.fetchall()
                                for pt in ptRecords:
                                    print(pt)
                                # print(json.dumps(d[hos_id]['patients'],indent=5))

                                print()
                            elif ch2==2:
                                nam=input("Enter the name of the Patient : ")
                                if nam=='5':
                                    break
                                else:
                                    id=input("Enter his/her Mail Address : ")
                                    if id=='5':
                                        break
                                    else:
                                        password=input("Enter his/her Password : ")
                                        if password=='5':
                                            break
                                        else:
                                            dis=input("What disease he/she have : ")
                                            if dis=='5':
                                                break
                                            else:
                                                pay=int(input("Enter the Charged Amount : ₹ "))
                                                if pay==5:
                                                    break
                                                else:
                                                    mob_num=input("Enter his/her Mobile Number : ")
                                                    if mob_num=='5':
                                                        break
                                                    else:

                                                        code = ""
                                                        hospname = dtl[0][3]
                                                        for word in hospname.split():
                                                            code = code + word[0].upper()
                                                    
                                                        patname = nam
                                                        for i in range(2):
                                                            code = code + patname[i].upper()

                                                        day = str(date.today())
                                                        daylist = day.split("-")
                                                        for i in range(2,-1,-1):
                                                            if i == 0:
                                                                yr = str(int(daylist[i]) - 2000)
                                                                code = code + yr
                                                            else:
                                                                code = code + daylist[i]

                                                        n=len(dtl[0][0])                
                                                        tblName=(dtl[0][0])[:(n-10)]
                                                        cur.execute("INSERT INTO %s value('%s', '%s', '%s', %s, '%s', '%s', '%s')"%(tblName, id, nam, dis, pay, mob_num, password, code))
                                                        con.commit()

                                                        cur.execute("UPDATE hospitalData SET PATIENT_COUNT=PATIENT_COUNT+1 WHERE NAME='%s'"%(dtl[0][3],))
                                                        con.commit()

                                                        cur.execute("UPDATE hospitalData SET EARNED=EARNED+%s WHERE NAME='%s'"%(pay, dtl[0][3],))
                                                        con.commit()


                                                        # d4={"Patient Name":nam,"Disease":dis,"Paid":pay,"Mobile Number":mob_num,"paswrd":password}
                                                        # d[hos_id]['patients'][id]=d4
                                                        # d[hos_id]["earned"]=d[hos_id]["earned"]+pay
                                                        # d[hos_id]["num_of_patients"]=d[hos_id]["num_of_patients"]+1
                                                        print("\nUpdated Successfully")
                            elif ch2==3:
                                cur.execute("Select EARNED from hospitalData WHERE MAIL='%s'"%(hos_id,))
                                earned=cur.fetchall()
                                print("\nTOTAL EARNED : ₹ ",earned[0][0])
                                m=input("Enter to continue...")
                            elif ch2==5:
                                break
                            else:
                                print("Sorry! Choice Have not Matched.")
                    elif b=="5":
                        break
                    else:
                        print('Incorrect Password! Please Try Again.')
            elif hos_id=="5":
                break
            else:
                print("You Have not Registered with our Platform. Please Register Yourself.\n")
                id=input("Please Enter Your Mail Address : ")
                if id=='5':
                    break
                else:
                    password=input("Enter A Strong Password : ")
                    if password=='5':
                        break
                    else:
                        hnam=input("Enter the full name of your Hospital : ")
                        if hnam=='5':
                            break
                        else:
                            addrs=input("Enter the Address of your Hospital : ")
                            if addrs=='5':
                                break
                            else:
                                cur.execute("INSERT into hospitalData VALUES('%s', %s, '%s', '%s', '%s', %s, '%s')"%(id, 0, password, hnam, addrs, 0, "Empty"))
                                con.commit()

                                n = len(id)
                                tblName=id[:(n-10)]
                                cur.execute("CREATE TABLE %s (PT_MAIL VARCHAR(25), PT_NAME VARCHAR(25), DISEASE VARCHAR(25), PAID INT, MOBILE CHAR(10), PSWD VARCHAR(25), CODE CHAR(10))"%(tblName))
                                con.commit()

                                cur.execute("Select * from hospitalData WHERE MAIL='%s'"%(id,))
                                dtl=cur.fetchall()
                                
                                print("\n.....You Are REGISTERED SUCCESSFULLY")
                                print("\n***********************",dtl[0][3],"***********************\n")
                                while True:

                                    print("---------------------------------------------------------")
                                    print("| Type:-                                                |")
                                    print("| 1 - Want to Check Patient Details                     |")
                                    print("| 2 - For Adding Data of Other Patients(Offline)        |")
                                    print("| 3 - To Check the Valuation of Your Hospital(Earned)   |")
                                    print("| 5 - to exit                                           |")
                                    print("---------------------------------------------------------\n")
                                    ch2=int(input("Enter Your Choice : "))
                                    if ch2==1:
                                        n=len(id)                
                                        tblName=(id)[:(n-10)]
                                        cur.execute("SELECT * FROM %s"%(tblName,))
                                        ptRecords = cur.fetchall()
                                        for pt in ptRecords:
                                            print(pt)
                                        # print(json.dumps(d[id]['patients'],indent=5))
                                        print()
                                    elif ch2==2:
                                        nam=input("Enter the name of the Patient : ")
                                        if nam=='5':
                                            break
                                        else:
                                            id2=input("Enter his/her Mail Address : ")
                                            if id2=='5':
                                                break
                                            else:
                                                password=input("Enter his/her Password : ")
                                                if password=='5':
                                                    break
                                                else:
                                                    dis=input("What disease he/she have : ")
                                                    if dis=='5':
                                                        break
                                                    else:
                                                        pay=int(input("Enter the Charged Amount : ₹ "))
                                                        if pay==5:
                                                            break
                                                        else:
                                                            mob_num=input("Enter his/her Mobile Number : ")
                                                            if mob_num=='5':
                                                                break
                                                            else:

                                                                code = ""
                                                                hospname = hnam
                                                                for word in hospname.split():
                                                                    code = code + word[0].upper()
                                                    
                                                                patname = nam
                                                                for i in range(2):
                                                                    code = code + patname[i].upper()

                                                                day = str(date.today())
                                                                daylist = day.split("-")
                                                                for i in range(2,-1,-1):
                                                                    if i == 0:
                                                                        yr = str(int(daylist[i]) - 2000)
                                                                        code = code + yr
                                                                    else:
                                                                        code = code + daylist[i]

                                                                n=len(id)                
                                                                tblName=(id[:(n-10)])
                                                                cur.execute("INSERT INTO %s values('%s', '%s', '%s', %s, '%s', '%s', '%s')"%(tblName, id2, nam, dis, pay, mob_num, password, code))
                                                                con.commit()

                                                                cur.execute("UPDATE hospitalData SET PATIENT_COUNT=PATIENT_COUNT+1 WHERE NAME='%s'"%(hnam,))
                                                                con.commit()

                                                                cur.execute("UPDATE hospitalData SET EARNED=EARNED+%s WHERE NAME='%s'"%(pay, hnam,))
                                                                con.commit()
                                                            
                                                                # d4={"Patient Name":nam,"Disease":dis,"Paid":pay,"Mobile Number":mob_num,"paswrd":password}
                                                                # d[id]["patients"][id2]=d4
                                                                # d[id]["earned"]=d[id]["earned"]+pay
                                                                # d[id]["num_of_patients"]=d[id]["num_of_patients"]+1
                                                                # d3={"paswrd":password,"name":nam,"Mobile Number":mob_num}
                                                                # d2[id]=d3

                                                                print("\nUpdated Successfully")
                                    elif ch2==3:
                                        cur.execute("Select EARNED from hospitalData WHERE MAIL='%s'"%(id,))
                                        earned=cur.fetchall()
                                        print("\nTOTAL EARNED : ₹ ",earned[0][0])
                                        
                                        m=input("Enter to continue...")
                                    elif ch2==5:
                                        break
                                    else:
                                        print("Sorry! Choice Have not Matched.")
    elif ch1==2:
        while True:
            print("---------------------------------------------------------")
            print("| Type:-                                                |")
            print("| 5 - to exit                                           |")
            print("---------------------------------------------------------\n")
            pat_id=input("Please enter your Login ID : ")

            cur.execute("Select MAIL from individualData WHERE MAIL='%s'"%(pat_id,))
            present=cur.fetchall()

            if present:
                while True:
                    print("---------------------------------------------------------")
                    print("| Type:-                                                |")
                    print("| 5 - to exit                                           |")
                    print("---------------------------------------------------------\n")
                    b=input('Please Enter your Password : ')

                    cur.execute("Select * from individualData WHERE MAIL='%s'"%(pat_id,))
                    dtl=cur.fetchall()

                    if b==dtl[0][1]:
                        print("\nHey There!!")
                        print("Welcome",dtl[0][2].upper(),"!\n")
                        while True:
                            print("---------------------------------------------------------")
                            print("| Type:-                                                |")
                            print("| 1 - To Book an Appointment                            |")
                            print("| 2 - To Check Previous Record                          |")
                            print("| 5 - to exit                                           |")
                            print("---------------------------------------------------------\n")
                            ch2=int(input("Enter Your Choice : "))
                            if ch2==1:
                                while True:
                                    hospitals=[]

                                    cur.execute("Select NAME from hospitalData WHERE PATIENT_COUNT<=3")
                                    names=cur.fetchall()

                                    for name in names:
                                        hospitals=hospitals+[name[0]]
                                    print("Hospitals Available Now : \n",hospitals)
                                    l=len(hospitals)
                                    ch3=input("Which Hospital Would You Like To Have (Enter Name) :\n")
                                    ch3=ch3.upper()
                                    if ch3=="5":
                                        break
                                    else:
                                        if ch3 in hospitals:
                                            print(json.dumps(rate,indent=5))
                                            dis=input("\nWhat Disease You Have?\n")
                                            dis=dis.capitalize()
                                            if dis=="5":
                                                break
                                            else:
                                                if dis in rate:
                                                            
                                                    cur.execute("Select * from hospitalData WHERE NAME='%s'"%(ch3,))
                                                    dtl=cur.fetchall()

                                                    cur.execute("Select * from individualData WHERE MAIL='%s'"%(pat_id,))
                                                    patient=cur.fetchall()

                                                    print()
                                                    print("------------------------------ APPOINTMENT ------------------------------")
                                                    print("|                                                                       |")
                                                    print("|                                                                       |")
                                                    print("| HOSPITAL'S NAME : ", dtl[0][3])
                                                    print("| HOSPITAL'S MAIL : ", dtl[0][0])
                                                    print("| HOSPITAL'S ADDRESS : ", dtl[0][4])
                                                    print("|                                                                       |")
                                                    print("|                                                                       |")
                                                    print("| PATIENT'S NAME : ", patient[0][2])
                                                    print("| PATIENT'S MAIL : ", patient[0][0])
                                                    print("| PATIENT'S MB. NUMBER : ", patient[0][3])
                                                    print("|                                                                       |")
                                                    print("|                                                                       |")
                                                    print("| DISEASE : ", dis)
                                                    print("| CHARGED AMOUNT : ₹ ", rate[dis])
                                                    print("| DATE OF APPOINTMENT : ", date.today())
                                                    print("|                                                                       |")
                                                    print("|                                                                       |")
                                                    print("-------------------------------------------------------------------------\n")
                                                    print("....take a sreenshot of the appointment.")

                                                    code = ""
                                                    hospname = dtl[0][3]
                                                    for word in hospname.split():
                                                        code = code + word[0].upper()
                                                    
                                                    patname = patient[0][2]
                                                    for i in range(2):
                                                        code = code + patname[i].upper()

                                                    day = str(date.today())
                                                    daylist = day.split("-")
                                                    for i in range(2,-1,-1):
                                                        if i == 0:
                                                            yr = str(int(daylist[i]) - 2000)
                                                            code = code + yr
                                                        else:
                                                            code = code + daylist[i]
                                                            
                                                    n=len(dtl[0][0])                
                                                    tblName=((dtl[0][0])[:(n-10)])    
                                                    cur.execute("INSERT INTO %s values('%s', '%s', '%s', %s, '%s', '%s', '%s')"%(tblName, patient[0][0], patient[0][2], dis, rate[dis], patient[0][3], patient[0][1], code))
                                                    con.commit()

                                                    cur.execute("UPDATE hospitalData SET PATIENT_COUNT=PATIENT_COUNT+1 WHERE NAME='%s'"%(dtl[0][3],))
                                                    con.commit()

                                                    cur.execute("UPDATE hospitalData SET EARNED=EARNED+%s WHERE NAME='%s'"%(rate[dis], dtl[0][3],))
                                                    con.commit()
                                                    n=input("Enter to Continue...\n")

                                                else:
                                                    print("Extremely Sorry! We don't have the Medication of this Disease.")
                                                    break
                                        else:   
                                            print("No such Hospital!")
                            elif ch2==2:

                                # Patient Records
                                cur.execute("SHOW TABLES")
                                mydb=cur.fetchall()
                                data = {}

                                for table in mydb:
                                    if table[0] != "hospitaldata" and table[0] != "individualdata":
                                        cur.execute("SELECT * FROM %s WHERE PT_NAME='%s' AND PSWD='%s'"%(table[0], dtl[0][2], dtl[0][1]))
                                        val=cur.fetchall()
                                        data[table[0] + "@gmail.com"] = val

                                # dtl={}
                                # for i in d:
                                #     x=d[i]['patients']
                                #     for j in x:
                                #         if j==pat_id:
                                #             q=d[i]['hos_name']
                                #             p=x[j]
                                #             dtl[q]=p

                                print(json.dumps(data,indent=5))
                            elif ch2==5:
                                break
                            else:
                                print("Sorry! Choice Have not Matched.")
                    elif b=="5":
                        break
                    else:
                        print('Incorrect Password! Please Try Again.')
            elif pat_id=="5":
                break
            else:
                print("We don't have such account. Please Register Yourself.\n")
                id=input("Please Enter Your Mail Address : ")
                if id=="5":
                    break
                else:
                    password=input("Enter A Strong Password : ")
                    if password=="5":
                        break
                    else:
                        nam=input("Kindly Enter your Name : ")
                        if nam=="5":
                            break
                        else:
                            mob_num=input("Please Enter Your Mobile Number : ")
                            if mob_num=="5":
                                break
                            else:

                                cur.execute("INSERT into individualData VALUE('%s', '%s', '%s', '%s')"%(id, password, nam, mob_num))
                                con.commit()

                                # d3={"paswrd":password,"name":nam,"Mobile Number":mob_num}
                                # d2[id]=d3

                                cur.execute("Select * from individualData WHERE MAIL='%s'"%(id,))
                                dtl=cur.fetchall()
                                
                                print("\n.....You Are REGISTERED SUCCESSFULLY\n\n")
                                while True:
                                    print("\nHey There!!")
                                    print("Welcome",dtl[0][2].upper(),"!\n")
                                    while True:
                                        print("---------------------------------------------------------")
                                        print("| Type:-                                                |")
                                        print("| 1 - To Book an Appointment                            |")
                                        print("| 2 - To Check Previous Record                          |")
                                        print("| 5 - to exit                                           |")
                                        print("---------------------------------------------------------\n")
                                        ch2=int(input("Enter Your Choice : "))
                                        if ch2==1:
                                            while True:
                                                hospitals=[]

                                                cur.execute("Select NAME from hospitalData WHERE PATIENT_COUNT<3")
                                                names=cur.fetchall()

                                                for name in names:
                                                    hospitals=hospitals+[name[0]]
                                                print("Hospitals Available Now : \n",hospitals)
                                                l=len(hospitals)
                                                ch3=input("Which Hospital Would You Like To Have (Enter Name) :\n")
                                                ch3=ch3.upper()
                                                if ch3=="5":
                                                    break
                                                else:
                                                    if ch3 in hospitals:
                                                        print(json.dumps(rate,indent=5))
                                                        dis=input("\nWhat Disease You Have?\n")
                                                        dis=dis.capitalize()
                                                        if dis=="5":
                                                            break
                                                        else:
                                                            if dis in rate:
                                                            
                                                                cur.execute("Select * from hospitalData WHERE NAME='%s'"%(ch3,))
                                                                dtl=cur.fetchall()

                                                                cur.execute("Select * from individualData WHERE MAIL='%s'"%(id,))
                                                                patient=cur.fetchall()


                                                                print()
                                                                print("------------------------------ APPOINTMENT ------------------------------")
                                                                print("|                                                                       |")
                                                                print("|                                                                       |")
                                                                print("| HOSPITAL'S NAME : ", dtl[0][3])
                                                                print("| HOSPITAL'S MAIL : ", dtl[0][0])
                                                                print("| HOSPITAL'S ADDRESS : ", dtl[0][4])
                                                                print("|                                                                       |")
                                                                print("|                                                                       |")
                                                                print("| PATIENT'S NAME : ", patient[0][2])
                                                                print("| PATIENT'S MAIL : ", patient[0][0])
                                                                print("| PATIENT'S MB. NUMBER : ", patient[0][3])
                                                                print("|                                                                       |")
                                                                print("|                                                                       |")
                                                                print("| DISEASE : ", dis)
                                                                print("| CHARGED AMOUNT : ₹ ", rate[dis])
                                                                print("| DATE OF APPOINTMENT : ", date.today())
                                                                print("|                                                                       |")
                                                                print("|                                                                       |")
                                                                print("-------------------------------------------------------------------------\n")
                                                                print("....take a sreenshot of the appointment.")

                                                                code = ""
                                                                hospname = dtl[0][3]
                                                                for word in hospname.split():
                                                                    code = code + word[0].upper()
                                                    
                                                                patname = patient[0][2]
                                                                for i in range(2):
                                                                    code = code + patname[i].upper()

                                                                day = str(date.today())
                                                                daylist = day.split("-")
                                                                for i in range(2,-1,-1):
                                                                    if i == 0:
                                                                        yr = str(int(daylist[i]) - 2000)
                                                                        code = code + yr
                                                                    else:
                                                                        code = code + daylist[i]

                                                                
                                                                n=len(dtl[0][0])                
                                                                tblName=((dtl[0][0])[:(n-10)])    
                                                                cur.execute("INSERT INTO %s value('%s', '%s', '%s', %s, '%s', '%s', '%s')"%(tblName, patient[0][0], patient[0][2], dis, rate[dis], patient[0][3], patient[0][1], code))
                                                                con.commit()

                                                                cur.execute("UPDATE hospitalData SET PATIENT_COUNT=PATIENT_COUNT+1 WHERE NAME='%s'"%(dtl[0][3],))
                                                                con.commit()

                                                                cur.execute("UPDATE hospitalData SET EARNED=EARNED+%s WHERE NAME='%s'"%(rate[dis], dtl[0][3],))
                                                                con.commit()
                                                                n=input("Enter to Continue...\n")

                                                            else:
                                                                print("Extremely Sorry! We don't have the Medication of this Disease.")
                                                                break
                                                    else:   
                                                        print("No such Hospital!")
                                                        break
                                        elif ch2==2:

                                            # Patient Records
                                            cur.execute("SHOW TABLES")
                                            mydb=cur.fetchall()
                                            data = {}

                                            for table in mydb:
                                                if table[0] != "hospitaldata" and table[0] != "individualdata":
                                                    cur.execute("SELECT * FROM %s WHERE PT_NAME='%s' AND PSWD='%s'"%(table[0], dtl[0][2], dtl[0][1]))
                                                    val=cur.fetchall()
                                                    data[table[0] + "@gmail.com"] = val

                                            # dtl={}
                                            # for i in d:
                                            #     x=d[i]['patients']
                                            #     for j in x:
                                            #         if j==pat_id:
                                            #             q=d[i]['hos_name']
                                            #             p=x[j]
                                            #             dtl[q]=p

                                            print(json.dumps(data,indent=5))
                                        elif ch2==5:
                                            break
                                        else:
                                            print("Sorry! Choice Have not Matched.")
    elif ch1==5:
        print("\n***************************************************** THANK YOU *****************************************************\n")
        con.commit()
        break
    else:
        print("INVALID Choice!!\n\n")