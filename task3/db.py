import sqlite3
conn = sqlite3.connect(r'C:\Users\mfarooqui2\Documents\Python Scripts\flas\test.db')
from flask import jsonify,json
# import json

# conn.execute('''CREATE TABLE Employee
#          (ID varchar(10) PRIMARY KEY     NOT NULL,
#          NAME           TEXT,
#          AGE            INT,
#          ADDRESS        VARCHAR(1000),
#          SALARY         REAL,
#          email Varchar(40),
#          Phone_no Varchar(20),
#          emp_image BLOB );''')

# dir (conn)
# with conn as f:
#     f.execute('''CREATE TABLE Emp_img
#          (Emp_ID INT PRIMARY KEY NOT NULL,
#          emp_image BLOB );''')
#     f.commit()
# with conn as f:
#     f.execute('''Drop TABLE Emp_img;''')
#     f.commit()

# with open(conn) as cru:
#     li=
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Paul1', 34, 'California', 20000.00 )");
# conn.commit()

# with conn as f:
#     f.execute('''INSERT INTO Employee  (ID ,NAME,AGE,ADDRESS,SALARY,email,Phone_no,emp_image)
#     Values("2","yun2",202,"anywh2",502,'mohamme@gmail2.com','019230982','');''')
#     f.commit()
tup= ('3', 'yun3', 203, 'anywh3', 50.0, 'mohamme@gmail3.com', '019230983', '')
with conn as f:
    f.execute('''INSERT INTO Employee  (ID ,NAME,AGE,ADDRESS,SALARY,email,Phone_no,emp_image)
    Values(?,?,?,?,?,?,?,?);''',tup)
	
	
	

	
	
	
	
	
