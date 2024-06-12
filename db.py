import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="6090",
    database="expense"
)
mycursor = mydb.cursor()

