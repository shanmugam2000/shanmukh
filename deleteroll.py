import sqlite3
connection = sqlite3.connect("college.db")

getroll=input("Enter RollNumber to be Deleted ? ")

connection.execute("delete from student where rollnumber="+getroll)
connection.commit()
print("Deleted succesfully")

for i in result:
         print("name =>", i[1])
         print("rollnumber =>", i[2])
         print("admno =>", i[3])
         print("college =>", i[4])