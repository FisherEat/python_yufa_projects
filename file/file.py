




with open('/Users/gl/python_test/tieba/TT.txt','w', encoding='utf-8') as file:
    file.write('我是高龙')

f = open('./TT.txt', 'r', encoding='utf-8', errors='ignore')

if f:
    print(f.read())
    f.close()


from io import  StringIO

f = StringIO()
f.write('hhhhhhh,gaolong')
print(f.getvalue())


import os
# print(os.name)
# print(os.environ)
# print(os.environ.get('PATH'))


import  json
d = dict(name='Bob', age=20, score=99)
print(json.dumps(d))

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
def studentdict(std):
    return {
        'name': std.name,
        'age':std.age,
        'score':std.score
    }

s = Student('hhh', 30, 90)
print(json.dumps(s, default=studentdict))

import psutil
print(psutil.cpu_count())

print(psutil.virtual_memory())

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount)