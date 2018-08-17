import sqlite3

# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
#
# create_string = 'create table user (id varchar(20) primary key, name varchar(20))'
# cursor.execute(create_string)
#
# insert_string = 'insert into user(id, name) values(\'1\', \'gaolong\')'
# cursor.execute(insert_string)
#
# print(cursor.rowcount)
#
# cursor.close()
#
# conn.commit()
#
# conn.close()

print('-----------------')
nextconn = sqlite3.connect('test.db')
nextcursor = nextconn.cursor()
print(nextcursor.execute('select * from user where id=?',('1',)))

print(nextcursor.fetchall())
nextcursor.close()
nextconn.close()