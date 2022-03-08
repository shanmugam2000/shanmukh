import sqlite3

connection = sqlite3.connect("college.db")

getroll=input("Enter rollnumber to be updated ? ")

getName=input("Enter New Name : ")
getAdmno=input("Enter New Admno : ")
getCollege=input("Enter New College : ")

connection.execute("UPDATE student \
 SET NAME= '"+getName+"',ADMNO="+getAdmno+",COLLEGE='"+getCollege+"' \
     WHERE ROLLNUMBER="+getroll)

connection.commit()
print("updated succesfully")

result = connection.execute("select * from student")
