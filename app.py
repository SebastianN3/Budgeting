from flask import Flask, render_template
import sqlite3
import os.path

app = Flask(__name__)

@app.route('/')
def index():
    # You don't have to specify the name of the folder. 
    # It knows it has to look into templates folder
    return render_template("index.html")


def create_database():
    # connecting to the database  
    connection = sqlite3.connect("./databases/myTable.db") 
    
    # cursor (This is a control structure used to traverse and fetch the records of the database)  
    cursor = connection.cursor() 
    
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE emp (  
    staff_number INTEGER PRIMARY KEY,  
    fname VARCHAR(20),  
    lname VARCHAR(30),  
    gender CHAR(1),  
    joining DATE);"""
    
    # execute the statement 
    cursor.execute(sql_command) 
    
    # SQL command to insert the data in the table 
    sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
    cursor.execute(sql_command) 
    
    # another SQL command to insert the data in the table 
    sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
    cursor.execute(sql_command) 
    
    # To save the changes in the files. Never skip this.  
    # If we skip this, nothing will be saved in the database. 
    connection.commit() 
    
    # close the connection 
    connection.close()


if __name__ == '__main__':
    # Create Database if it does not exist
    if (not os.path.isfile("./databases/myTable.db")):
        create_database()
    
    # Run server 
    app.run(debug=True)