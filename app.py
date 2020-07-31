from flask import Flask, render_template
import sqlite3
import os.path
# from blueprints.test.blueprintTest import test
import blueprints.budget.budget as budget

app = Flask(__name__)

# Register my Blueprint
# url_prefix marks the start of the url to send to the blueprint
# In this case: if /admin/test is requested, the blueprint will receive /test
app.register_blueprint(budget.add, url_prefix="/budget")

@app.route('/')
def index():
    # You don't have to specify the name of the folder. 
    # It knows it has to look into templates folder
    return render_template("index.html")


def create_database():
    # connecting to the database  
    connection = sqlite3.connect("./databases/budget.db") 
    
    # cursor (This is a control structure used to traverse and fetch the records of the database)  
    cursor = connection.cursor() 
    
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE expense (  
    id INTEGER PRIMARY KEY,  
    item VARCHAR(80),  
    label VARCHAR(20),  
    price FLOAT,  
    purchased DATE);"""
    
    # execute the statement 
    cursor.execute(sql_command) 
    
    # To save the changes in the files. Never skip this.  
    # If we skip this, nothing will be saved in the database. 
    connection.commit() 
    
    # close the connection 
    connection.close()


if __name__ == '__main__':
    # Create Database if it does not exist
    if (not os.path.isfile("./databases/budget.db")):
        create_database()
    
    # Run server 
    app.run(debug=True)