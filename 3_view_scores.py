import sqlite3  
  
conn = sqlite3.connect('game1.db')  
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