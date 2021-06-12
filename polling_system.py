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

def main_account_screen():
    global main_screen

    main_screen = Tk()
    main_screen.geometry("300x350")
    main_screen.title("Account Login")
 
    Label(text="SCHOOL COUNCIL VOTING MACHINE", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
    
    Button(text="Login", height="2", width="30", command = login).pack() 
    Label(text="").pack() 
    
    Button(text="Register", height="2", width="30", command = register).pack()
    Label(text="").pack()

    Button(text="Vote", height="2", width="30", command = vote).pack() 
    Label(text="").pack()

    Button(text="See Results", height="2", width="30", command = results).pack() 
    Label(text="").pack() 

    main_screen.mainloop() # start the GUI
 
main_account_screen() 
