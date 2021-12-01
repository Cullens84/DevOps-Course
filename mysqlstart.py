import mysql.connector
# imports the connector for mysql

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="12Oranges!",
                             database="DFECloud2")

# code to connect to the database,

C = db.cursor()
# creates the instance for the data to be stored and then executed by c.execute command later in the code

choice = "y"
# creating the variable

while choice == "y":
    # creating the loop parameter

    registration = input("enter your registration number:")
# creating user input to populate the query to enter to the database
    name = input("enter your name:")
# creating user input to populate the query to enter to the database
    marks = input("enter your marks:")
# creating user input to populate the query to enter to the database

    sqlquery = "insert into school values({0},'{1}',{2})".format(
        registration, name, marks)
# this is the body of the query to send, the three boxes with the number are placeholders
# these place holders relate to the format string format(registration,name,marks)

C.execute(sqlquery)
# command to send to sql with input

choice = input("do you want to add anopther record(y/n):")
# creating the option to fulfil the loop and stop or add another
db.commit()
# this commits the query to the database
