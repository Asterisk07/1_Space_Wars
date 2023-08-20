import sqlite3  
import os
import sys
# Get the directory path of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))
# Set the current working directory to the script's directory
os.chdir(script_directory)
conn = sqlite3.connect('../../data/game1.db') 
cur=conn.cursor()
print("Opened database successfully")
q = """SELECT * from SCores;"""
# q="""UPDATE scores    SET Name='New',score=-1    WHERE id = 1;"""

cur.execute(q)
d=cur.fetchall()
print(len(d))
for i in d:
    print(i)
conn.commit()
conn.close()