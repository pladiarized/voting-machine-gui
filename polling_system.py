from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1212",
  database="records" #add after creating database on line 12
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE records")
#mycursor.execute("CREATE TABLE details (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), fullname VARCHAR(255), sectionclass VARCHAR(255), post VARCHAR(255), votes INTEGER(255))")
