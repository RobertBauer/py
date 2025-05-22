import pyodbc 

#cnxn = pyodbc.connect('DRIVER={Oracle in OraClient12Home1};Host=192.168.0.14;Service Name=asmacsdb;User ID=emp;Password=emp')
cnxn = pyodbc.connect('DRIVER={Oracle in OraClient12Home1};DBQ=192.168.0.14:1521/asmacsdb; UID=emp;PWD=emp')

cursor = cnxn.cursor()
cursor.execute("INSERT INTO EMP (EMPNO, ENAME, JOB, MGR) VALUES (535, 'Robert', 'Manager', 545)") 

cursor = cnxn.cursor()	
cursor.execute("SELECT * FROM EMP") 
row = cursor.fetchone() 
while row:
    print (row) 
    row = cursor.fetchone()
cursor.close()
cnxn.close()

