import sqlite3
connection = sqlite3.connect("college.db")
getroll = input("enter the rollnumber to be searched ? ")
result = connection.execute("select * from student where rollnumber="+getroll)

for i in result:
    print("name =>",i[1])
    print("rollnumber =>",i[2])
    print("admno =>",i[3])
    print("college =>",i[4])