import  mysql.connector

conn = mysql.connector.connect(user='root', password='',database='guest', use_unicode=True)

cursor = conn.cursor()

cursor.execute('select * from user where id = %s', ('1',))

print(cursor.fetchall())