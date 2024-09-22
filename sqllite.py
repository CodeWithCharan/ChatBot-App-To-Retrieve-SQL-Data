import sqlite3

# create a variable for connection
connection = sqlite3.connect("students.db")

# create a cursor object to insert records and a create table
cursor = connection.cursor()

# create a table
table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

# execute the table
cursor.execute(table_info)

# insert records
cursor.execute('''Insert Into STUDENT values('Charan','GenAI','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sushanth','Web dev','B',100)''')
cursor.execute('''Insert Into STUDENT values('Veekshith','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Dheeraj','Content Creation','A',89)''')
cursor.execute('''Insert Into STUDENT values('Rathan','Data Science','A',65)''')
cursor.execute('''Insert Into STUDENT values('Deekshith','Automation Testing','B',55)''')
cursor.execute('''Insert Into STUDENT values('Tyson','Web dev','B',50)''')

# query to cisplay all the records
data = cursor.execute("SELECT * FROM STUDENT")

# display all the records in terminal
print("Student database:")
for student in data:
    print(student)

# commit the changes
connection.commit()
# close the connection
connection.close()