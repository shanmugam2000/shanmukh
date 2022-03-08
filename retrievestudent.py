import sqlite3
connection = sqlite3.connect("college.db")

result = connection.execute("select * from student")

for i in result:
    print("name",i[1])
    print("rollnumber",i[2])
    print("admno ",i[3])
    print("college ",i[4])