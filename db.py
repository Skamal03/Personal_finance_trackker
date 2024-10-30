import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="enter_user",
    password="enter_passwor",
    database="expense"
)
mycursor = mydb.cursor()

