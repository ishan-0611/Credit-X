import sqlite3

conn = sqlite3.connect('CreditX.db')

c = conn.cursor()
c.execute('Select * from Payments;')

for row in c:
    print(row)

conn.close()
