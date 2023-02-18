import sqlite3  
from tkinter import messagebox as mb
conn = sqlite3.connect('game1.db')  
cur=conn.cursor()
print("Opened database successfully")

# q = """INSERT INTO scores VALUES (1,"New",0);"""
# q = """delete from scores;"""


conn.execute(q)
conn.commit()
conn.close()
mb.showinfo("","success")