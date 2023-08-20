import sqlite3  
import os
import sys
# Get the directory path of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))
# Set the current working directory to the script's directory
os.chdir(script_directory)
conn = sqlite3.connect('../../data/game1.db')  
from tkinter import messagebox as mb
cur=conn.cursor()
print("Opened database successfully")

# q = """INSERT INTO scores VALUES (1,"New",0);"""
# q = """delete from scores;"""


conn.execute(q)
conn.commit()
conn.close()
mb.showinfo("","success")