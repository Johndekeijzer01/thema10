import pymssql
conn = pymssql.connect(host='johndekeijzerserver.database.windows.net', port=1433,
database='Thema10', user='john@johndekeijzerserver', password='Junior130304')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Klant;')
row = cursor.fetchone()
while row:
 #Doe iets met deze rows
 print(str(row[0]) + ' \t' + str(row[1]) + ' ' + str(row[2]) + ' ' + str(row[3]) + ' ' + str(row[4]))
 row = cursor.fetchone()

conn.commit()
conn.close() 
