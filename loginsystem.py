# import libraries needed
import pandas as pd
import mysql.connector
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()


def welcome():
    print('''Hello, you are welcome to MyStudentPortalSystem, 
Kindly Fill in the following details to Get registered. 
Thanks''')


def login_access():
    user = int(input('Press 1 if you are a new user and 2 for an old user:'))
    if user == 1:
        store_user_input()
    elif user == 2:
        print('Enter your user name and password to proceed')


# create connection object to the sql local database
# use the dotenv method to hide important information
connection = mysql.connector.connect(host=os.getenv("HOST"),
                                     user=os.getenv("USERNAME"),
                                     password=os.getenv("PSWD"),
                                     port=os.getenv("PORT"),
                                     auth_plugin='mysql_native_password',
                                     database='Loginportal')
# create a cursor object
mycursor = connection.cursor()


# create a database called Loginportal and table user
# mycursor.execute('CREATE DATABASE Loginportal')
# create user table and insert columns into it
def create_table():
    mycursor.execute('''CREATE TABLE user (
                        user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                        user_name VARCHAR(50),
                        password VARCHAR(20),
                        username VARCHAR(30),
                        year_of_birth INTEGER,
                        department VARCHAR(20),
                        gender VARCHAR(15)
                    )''')


# sql query that inserts values into the database
sql = '''INSERT INTO user (user_name,password,fullname,year_of_birth,department,gender)
         VALUES (%s,%s,%s,%s,%s,%s)'''


# takes is the user inputs
def data_input():
    data = ()
    username = str(input("Please enter your username: "))
    password = str(input("Please enter your password: "))
    fullname = str(input("Please enter your fullname: "))
    year_of_birth = int(input("Please enter your year of birth: "))
    department = str(input("Please enter your department: "))
    gender = str(input("Please enter your gender: "))
    data = (username, password, fullname, year_of_birth, department, gender)
    return data


# creates a function that executes and saves the data into the database
def store_user_input():
    mycursor.execute(sql, data_input())
    connection.commit()


# function allows new or registered users to login
def login_page():
    welcome()
    login_access()


# login_page()

sql_select = '''
                DECLARE @user_input VARCHAR;
                SET @user_input = 2;
                SELECT user_name, department,year_of_birth, password
                FROM user
                WHERE user_name= @user_input;
            '''
mycursor = connection.cursor()
myresult1 = mycursor.execute(sql_select, multi=True)
myresult1 = mycursor.fetchall()
for data in myresult1:
    print(data)



