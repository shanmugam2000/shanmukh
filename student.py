import sqlite3

connection = sqlite3.connect("college.db")

connection.execute(''' create table student(
                       id integer primary key autoincrement,
                       name text,
                       rollnumber integer,
                       admno integer,
                       college text
                       
               


);   ''')

print("table created successfully")