# import libraries needed
import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def welcome():
    print('''Hello, you are welcome to MyStudentPortalSystem, 
Kindly Fill in the following details to Get registered. 
Thanks''')


# create connection object to the sql local database
# create a cursor object for connection
# use the dotenv method to hide important information


connection = mysql.connector.connect(host=os.getenv("HOST"),
                                     user=os.getenv("USERNAME"),
                                     password=os.getenv("PSWD"),
                                     port=os.getenv("PORT"),
                                     auth_plugin='mysql_native_password',
                                     database='Loginportal')

mycursor = connection.cursor()

# create a database called Loginportal and table user
# mycursor.execute('CREATE DATABASE Loginportal')
# create user table and insert columns into it

# create_table = mycursor.execute('''CREATE TABLE course (
#                         user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
#                         user_name VARCHAR(50),
#                         password VARCHAR(20),
#                         username VARCHAR(30),
#                         year_of_birth INTEGER,
#                         department VARCHAR(20),
#                         gender VARCHAR(15)
#                         )''')
#
# connection.commit()

# create_table()

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


def login_access():
    user = int(input('Press 1 if you are a new user and 2 for an old user:'))
    if user == 1:
        store_user_input()
        print(input('PRESS ENTER TO RETURN TO LOGIN PAGE:'))
        print('Please enter your username and password')
        pass

    elif user == 2:
        print('Enter your user name and password to proceed')
        #pass
        #user_login()
login_access()

# using a parameterised query to store variable in sql
sql_select = '''
                SELECT user_name, password, fullname
                FROM Loginportal.user
                WHERE user_name= %s
                AND password= %s
            '''


username = str(input('Please enter your username:'))
password = str(input('Please enter your password:'))
mycursor = connection.cursor()
result = mycursor.execute(sql_select, (username, password), )
result = mycursor.fetchall()
result_tuple = tuple(result)


def login_access():
    db_username = result_tuple[0][0]
    db_password = result_tuple[0][1]
    if username == db_username and password == db_password:
        print('Login Successful!' '\n'
              'Welcome', '!')
        print(input('Press ENTER to continue'))




# checks user details and allows login or not
def user_login():
    if result_tuple == ():
        print('Username or password does not match.' '\n'
              'login unsuccessful, Please try again')
    else:
        login_access()

user_login()


# create a while loop to limit number of login attempts
