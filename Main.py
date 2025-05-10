import json
import pickle
from datetime import date

file=open("Hospital Data.txt", "rb+")
file2=open("Individual Data.txt", "rb+")
file3=open("Date.txt", "rb+")
d={}
try:
    while True:
        d=pickle.load(file)
except EOFError:
    pass
print("\n***************************** WELCOME TO COMBINED NETWORK OF ALL HOSPITALS AND PATIENTS *****************************\n")
earn=0
d2={}
try:
    while True:
        d2=pickle.load(file2)
except EOFError:
    pass
try:
    while True:
        s=pickle.load(file3)
except EOFError:
    pass
if s==date.today():
    pass
else:
    for i in d:
        d[i]['num_of_patients']=0
        s=date.today()                                                                                                               # Renewing Patients For Today as ZERO
rate={'Fever':3000,'Cold':3700,'Food Poisoning':5600}
while True:
    print("---------------------------------------------------------  ------------ For Example [ALREADY REGISTERED] -----------")
    print("| Type:-                                                |  | ID : vhospital@gmail.com     PASS : 123v@             |")
    print("| 1 - If you are entering as a Hospital                 |  | ID : orthohos@gmail.com     PASS : ortho123           |")
    print("| 2 - If you are entering as a Patient                  |  | ID : aditya@gmail.com     PASS : aditya@123           |")
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
            if hos_id in d:
                while True:
                    print("---------------------------------------------------------")
                    print("| Type:-                                                |")
                    print("| 5 - to exit                                           |")
                    print("---------------------------------------------------------\n")

                    b=input('Please Enter your Password : ')
                    if b==d[hos_id]['paswrd']:
                        print("\n***********************",d[hos_id]['hos_name'],"***********************\n")
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
                                print(json.dumps(d[hos_id]['patients'],indent=5))
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
                                                        d4={"Patient Name":nam,"Disease":dis,"Paid":pay,"Mobile Number":mob_num,"paswrd":password}
                                                        d[hos_id]['patients'][id]=d4
                                                        d[hos_id]["earned"]=d[hos_id]["earned"]+pay
                                                        d[hos_id]["num_of_patients"]=d[hos_id]["num_of_patients"]+1
                                                        print("\nUpdated Successfully")
                            elif ch2==3:
                                print("\nTOTAL EARNED : ₹ ",d[hos_id]["earned"])
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
                        nam=input("Enter the full name of your Hospital : ")
                        if nam=='5':
                            break
                        else:
                            addrs=input("Enter the Address of your Hospital : ")
                            if addrs=='5':
                                break
                            else:
                                d3={"num_of_patients":0,"paswrd":password,"hos_name":nam,"address":addrs,"earned":0,"patients":{}}
                                d[id]=d3
                                print("\n.....You Are REGISTERED SUCCESSFULLY")
                                print("\n***********************",d[id]['hos_name'],"***********************\n")
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
                                        print(json.dumps(d[id]['patients'],indent=5))
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
                                                                d4={"Patient Name":nam,"Disease":dis,"Paid":pay,"Mobile Number":mob_num,"paswrd":password}
                                                                d[id]["patients"][id2]=d4
                                                                d[id]["earned"]=d[id]["earned"]+pay
                                                                d[id]["num_of_patients"]=d[id]["num_of_patients"]+1
                                                                d3={"paswrd":password,"name":nam,"Mobile Number":mob_num}
                                                                d2[id]=d3
                                                                print("\nUpdated Successfully")
                                    elif ch2==3:
                                        print("\nTOTAL EARNED : ₹ ",d[id]["earned"])
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
            if pat_id in d2:
                while True:
                    print("---------------------------------------------------------")
                    print("| Type:-                                                |")
                    print("| 5 - to exit                                           |")
                    print("---------------------------------------------------------\n")
                    b=input('Please Enter your Password : ')
                    if b==d2[pat_id]['paswrd']:
                        print("\nHey There!!")
                        print("Welcome",d2[pat_id]['name'].upper(),"!\n")
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
                                    for i in d:
                                        if d[i]['num_of_patients']<3:
                                            hospitals=hospitals+[d[i]['hos_name']]
                                    print("Hospitals Available Now : \n",hospitals)
                                    l=len(hospitals)
                                    ch3=input("Which Hospital Would You Like To Have (Enter Name) :\n").upper()
                                    if ch3=="5":
                                        break
                                    else:
                                        if ch3 in hospitals:
                                            print(json.dumps(rate,indent=5))
                                            dis=input("\nWhat Disease You Have?\n").capitalize()
                                            if dis=="5":
                                                break
                                            else:
                                                if dis in rate:
                                                    for j in d:
                                                        if d[j]['hos_name']==ch3:
                                                            ad=d[j]['address']
                                                            mail=j
                                                            print()
                                                            print("------------------------------ APPOINTMENT ------------------------------")
                                                            print("|                                                                       |")
                                                            print("|                                                                       |")
                                                            print("| HOSPITAL'S NAME : ",ch3)
                                                            print("| HOSPITAL'S MAIL : ",mail)
                                                            print("| HOSPITAL'S ADDRESS : ",ad)
                                                            print("|                                                                       |")
                                                            print("|                                                                       |")
                                                            print("| PATIENT'S NAME : ",d2[pat_id]['name'])
                                                            print("| PATIENT'S MAIL : ",pat_id)
                                                            print("| PATIENT'S MB. NUMBER : ",d2[pat_id]['Mobile Number'])
                                                            print("|                                                                       |")
                                                            print("|                                                                       |")
                                                            print("| DISEASE : ",dis)
                                                            print("| CHARGED AMOUNT : ₹ ",rate[dis])
                                                            print("| DATE OF APPOINTMENT : ",date.today())
                                                            print("|                                                                       |")
                                                            print("|                                                                       |")
                                                            print("-------------------------------------------------------------------------\n")
                                                            print("....take a sreenshot of the appointment.")
                                                            w={"Patient Name":d2[pat_id]['name'],"Disease":dis,"Paid":rate[dis],"Mobile Number":d2[pat_id]['Mobile Number'],"paswrd":d2[pat_id]['paswrd']}
                                                            d[mail]['patients'][pat_id]=w
                                                            d[mail]["num_of_patients"]=d[mail]["num_of_patients"]+1
                                                            d[mail]["earned"]=d[mail]["earned"]+rate[dis]
                                                            n=input("Enter to Continue...\n")
                                                else:
                                                    print("Extremely Sorry! We don't have the Medication of this Disease.")
                                                    break
                                        else:   
                                            print("No such Hospital!")
                            elif ch2==2:
                                dtl={}
                                for i in d:
                                    x=d[i]['patients']
                                    for j in x:
                                        if j==pat_id:
                                            q=d[i]['hos_name']
                                            p=x[j]
                                            dtl[q]=p
                                print(json.dumps(dtl,indent=5))
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
                                d3={"paswrd":password,"name":nam,"Mobile Number":mob_num}
                                d2[id]=d3
                                print("\n.....You Are REGISTERED SUCCESSFULLY\n\n")
                                while True:
                                    print("\nHey There!!")
                                    print("Welcome",d2[id]['name'].upper(),"!\n")
                                    print("---------------------------------------------------------")
                                    print("| Type:-                                                |")
                                    print("| 1 - To Book an Appointment                            |")
                                    print("| 2 - To Check Previous Record                          |")
                                    print("| 5 - to exit                                           |")
                                    print("---------------------------------------------------------\n")
                                    ch2=int(input("Enter Your Choice : "))
                                    if ch2==1:
                                        hospitals=[]
                                        while True:
                                            for i in d:
                                                if d[i]['num_of_patients']<3:
                                                    hospitals=hospitals+[d[i]['hos_name']]
                                            print("Hospitals Available Now : \n",hospitals)
                                            l=len(hospitals)
                                            ch3=input("Which Hospital Would You Like To Have (Enter Name) :\n")
                                            if ch3=="5":
                                                break
                                            else:
                                                if ch3 in hospitals:
                                                    print(json.dumps(rate,indent=5))
                                                    dis=input("\nWhat Disease You Have?\n")
                                                    if dis in rate:
                                                        for j in d:
                                                            if d[j]['hos_name']==ch3:
                                                                ad=d[j]['address']
                                                                mail=j
                                                        print()
                                                        print("------------------------------ APPOINTMENT ------------------------------")
                                                        print("|                                                                       |")
                                                        print("|                                                                       |")
                                                        print("| HOSPITAL'S NAME : ",ch3)
                                                        print("| HOSPITAL'S MAIL : ",mail)
                                                        print("| HOSPITAL'S ADDRESS : ",ad)
                                                        print("|                                                                       |")
                                                        print("|                                                                       |")
                                                        print("| PATIENT'S NAME : ",nam)
                                                        print("| PATIENT'S MAIL : ",id)
                                                        print("| PATIENT'S MB. NUMBER : ",mob_num)
                                                        print("|                                                                       |")
                                                        print("|                                                                       |")
                                                        print("| DISEASE : ",dis)
                                                        print("| CHARGED AMOUNT : ₹ ",rate[dis])
                                                        print("| DATE OF APPOINTMENT : ",date.today())
                                                        print("|                                                                       |")
                                                        print("|                                                                       |")
                                                        print("-------------------------------------------------------------------------\n")
                                                        print("....take a sreenshot of the appointment.")
                                                        w={"Patient Name":nam,"Disease":dis,"Paid":rate[dis],"Mobile Number":mob_num,"paswrd":password}
                                                        d[mail]['patients'][id]=w
                                                        d[mail]["num_of_patients"]=d[mail]["num_of_patients"]+1
                                                        d[mail]["earned"]=d[mail]["earned"]+rate[dis]
                                                        n=input("Enter to Continue...\n")
                                                    else:
                                                        print("Extremely Sorry! We don't have the Medication of this Disease.")
                                                    break
                                                else:
                                                    print("No such Hospital!")
                                    elif ch2==2:
                                        dtl={}
                                        for i in d:
                                            x=d[i]['patients']
                                            for j in x:
                                                if j==id:
                                                    q=d[i]['hos_name']
                                                    p=x[j]
                                                    dtl[q]=p
                                        print(json.dumps(dtl,indent=5))
                                    elif ch2==5:
                                        break
                                    else:
                                        print("Sorry! Choice Have not Matched.")
    elif ch1==5:
        print("\n***************************************************** THANK YOU *****************************************************\n")
        pickle.dump(d,file)
        pickle.dump(d2,file2)
        pickle.dump(s,file3)
        file.close()
        file2.close()
        file3.close()
        break
    else:
        print("INVALID Choice!!\n\n")