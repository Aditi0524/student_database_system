import mysql.connector
import tkinter as tk

# Backend
def studentData():
    # Establish a connection to your MySQL server
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="aditi",
        password="root",
    )
    cur = con.cursor()

    # Dropping database 'student' if it already exists
    cur.execute("DROP DATABASE IF EXISTS student")

    # Preparing query to create a database
    sql = "CREATE DATABASE student"

    # Creating database
    cur.execute(sql)
    print('Database created successfully')
    
    # Switch to the 'student' database
    cur.execute("USE student")

    # Create the 'admission' table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS admission (
            StdID VARCHAR(255) PRIMARY KEY,
            Firstname VARCHAR(255),
            Surname VARCHAR(255),
            DoB DATE,
            Age VARCHAR(255),
            Gender VARCHAR(255),
            Address VARCHAR(255),
            Mobile VARCHAR(255)
        )
    """)
    con.commit()
    con.close()

def addStdRec(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="aditi",
        password="root",
        database="student")
    cur = con.cursor()

    # Insert a new record into the 'admission' table
    cur.execute("""
        INSERT INTO admission (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    
    con.commit()
    con.close()

def viewData():
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="aditi",
        password="root",
        database="student")
    cur = con.cursor()

    # View record in the 'admission' table
    cur.execute("SELECT * FROM admission")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows
    
def deleteRec(StdID):
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="aditi",
        password="root",
        database="student")
    cur = con.cursor()

    # Delete the record from the 'admission' table with the given ID
    cur.execute("DELETE FROM admission WHERE StdID=%s", (StdID,))

    con.commit()
    con.close()

def searchData(StdID="", Firstname="", Surname="",DoB="", Age="", Gender="", Address="", Mobile=""):
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="aditi",
        password="root",
        database="student")
    cur = con.cursor()

    # Search the record from the 'admission' table
    cur.execute("SELECT * FROM admission WHERE StdID=%s OR Firstname=%s OR Surname=%s OR DoB=%s OR Age=%s OR Gender=%s OR Address=%s OR Mobile=%s",(StdID, Firstname,Surname,DoB,Age, Gender,Address,Mobile))
    rows = cur.fetchall()

    con.commit()   
    con.close()
    return rows
    
def dataUpdate(StdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="aditi",
        password="root",
        database="student")
    cur = con.cursor()

    # Search the record from the 'admission' table
    cur.execute("UPDATE admission SET Firstname=%s, Surname=%s, DoB=%s, Age=%s, Gender=%s, Address=%s, Mobile=%s WHERE StdID=%s", (Firstname, Surname, DoB, Age, Gender, Address, Mobile, StdID))
    con.commit()
    con.close()

# Initialize the student data table
studentData()
