import pyodbc 

def print_emp_dept_join(connection=None):
    """
    Joins EMP and DEPT tables and prints the results on the screen.
    
    Args:
        connection: Optional pyodbc connection object. If None, creates a new connection.
    """
    # Use provided connection or create a new one
    if connection is None:
        cnxn = pyodbc.connect('DRIVER={Oracle in OraClient12Home1};DBQ=192.168.0.14:1521/asmacsdb; UID=emp;PWD=emp')
        close_connection = True
    else:
        cnxn = connection
        close_connection = False
    
    try:
        cursor = cnxn.cursor()
        # Join EMP and DEPT tables on DEPTNO
        cursor.execute("""
            SELECT e.EMPNO, e.ENAME, e.JOB, e.MGR, e.HIREDATE, e.SAL, e.COMM, 
                   d.DEPTNO, d.DNAME, d.LOC
            FROM EMP e
            LEFT JOIN DEPT d ON e.DEPTNO = d.DEPTNO
            ORDER BY e.EMPNO
        """)
        
        # Print header
        print("\n" + "="*100)
        print(f"{'EMPNO':<8} {'ENAME':<12} {'JOB':<12} {'MGR':<8} {'HIREDATE':<12} {'SAL':<8} {'COMM':<8} {'DEPTNO':<8} {'DNAME':<15} {'LOC':<15}")
        print("="*100)
        
        # Fetch and print rows
        row = cursor.fetchone()
        while row:
            empno = row[0] if row[0] else ''
            ename = row[1] if row[1] else ''
            job = row[2] if row[2] else ''
            mgr = row[3] if row[3] else ''
            hiredate = row[4].strftime('%Y-%m-%d') if row[4] else ''
            sal = row[5] if row[5] else ''
            comm = row[6] if row[6] else ''
            deptno = row[7] if row[7] else ''
            dname = row[8] if row[8] else ''
            loc = row[9] if row[9] else ''
            
            print(f"{str(empno):<8} {str(ename):<12} {str(job):<12} {str(mgr):<8} {str(hiredate):<12} {str(sal):<8} {str(comm):<8} {str(deptno):<8} {str(dname):<15} {str(loc):<15}")
            row = cursor.fetchone()
        
        print("="*100 + "\n")
        cursor.close()
        
    finally:
        if close_connection:
            cnxn.close()

#cnxn = pyodbc.connect('DRIVER={Oracle in OraClient12Home1};Host=192.168.0.14;Service Name=asmacsdb;User ID=emp;Password=emp')
cnxn = pyodbc.connect('DRIVER={Oracle in OraClient12Home1};DBQ=192.168.0.14:1521/asmacsdb; UID=emp;PWD=emp')

cursor = cnxn.cursor()
# Delete the record if it exists to avoid duplicate key error
cursor.execute("DELETE FROM EMP WHERE EMPNO = 535")
cursor.execute("INSERT INTO EMP (EMPNO, ENAME, JOB, MGR) VALUES (535, 'Robert', 'Manager', 545)") 
cnxn.commit()

cursor = cnxn.cursor()	
cursor.execute("SELECT * FROM EMP") 
row = cursor.fetchone() 

while row:
    print (row) 
    row = cursor.fetchone()

cursor.close()

# Call the function to join and print EMP and DEPT data
print_emp_dept_join(cnxn)

cnxn.close()

