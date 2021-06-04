import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1212",
  database="class12"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE class12")
#mycursor.execute("CREATE TABLE student (Admn_No INT PRIMARY KEY, name VARCHAR(255), class VARCHAR(255), roll int)")
#mycursor.execute("DROP TABLE student")
#mycursor.execute("INSERT INTO student(Admn_No, name, class, roll) VALUES (1234, 'hero', 'XII-D', 37);")
#mycursor.execute("desc student")
#mycursor.execute("SELECT * FROM student")
#result = mycursor.fetchall()
#for row in result:
    #print(row, '\n')
    
mydb.commit()