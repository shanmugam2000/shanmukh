import sqlite3

connection = sqlite3.connect("college.db")

#connection.execute(''' create table student(
#                    id integer primary key autoincrement,
#                     name text,
#                     rollnumber integer,
#                     admno integer,
#                     college text
                       
               
#);   ''')

print("table created successfully")
getName = input("Enter Name : ")
getRollNumber = input("Enter RollNumber : ")
getAdmno = input("Enter Admno : ")
getCollege = input("Enter College name : ")
connection.execute("INSERT INTO student(name,rollnumber,admno,college) \
    VALUES('"+getName+"',"+getRollNumber+","+getAdmno+",'"+getCollege+"')")
connection.commit()
connection.close()
print("Inserted succesfully")