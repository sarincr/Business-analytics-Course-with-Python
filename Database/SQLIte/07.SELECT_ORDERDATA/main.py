import sqlite3

 
X = sqlite3.connect('NeDB.db')
 
Y = X.cursor()

 
Y.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE (
         	ID integer,
         	Name text NOT NULL,
         	Date_Join text,
            Place text,
            Salary integer,
            Age real);''')

 
Y.execute("INSERT INTO Employee VALUES (1,'John','2020-03-01','Kerala',32,25000),(2,'Adam','2020-01-01','TN',22,30000),(3,'Mary','2022-01-01','Karnataka',24,120000)")

for row in Y.execute('SELECT * FROM Employee ORDER BY Date_Join'):
        print(row)

        
X.commit()

Y.close()
