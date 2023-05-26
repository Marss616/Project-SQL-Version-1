# Backend of Project SQL 

import mysql.connector

### Connect to the SLQ server

# Define your server details
host = '192.168.116.164' 
user = 'jack' 
password = 'User12345678!!' 

cnx = mysql.connector.connect(host=host,user=user,password=password)

cursor = cnx.cursor()

### End Connect to SQL server 
def show_databases():
    cursor.execute("SHOW DATABASES") # Fetch all database names
    print("Databases on the server:") # Print databases in the terminal 
    for db in cursor:
        print(db[0])

def testdef():
    print("1")

testdef()
show_databases()

cursor.close()
cnx.close()
