
import hashlib
import json
from functools import reduce
import re
import mysql.connector
import pandas as pd
import numpy as np

import argparse

print('----------------------分割线--------------')
# 哈希和序列化
md5 = hashlib.md5()
md5.update('how to use md5 in python'.encode('utf-8'))
print(md5.hexdigest())

d = dict(name='Bob', age=20,score=90)
print(json.dumps(d))

json_str = '{"name": "Bob", "age": 20, "score": 90, "result":true}'
print(json.loads(json_str))

adict = json.loads(json_str)
print(adict)
print('----------------------分割线--------------')

# 类 & 序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

a = Student('Bob', 20, 88)
print(json.dumps(a, default=student2dict))

print(json.dumps(a, default=lambda  obj: obj.__dict__))
print('----------------------分割线--------------')

# 高阶map\reduce
def f(x):
    return x*x
r = map(f, [1,2,3,4,45,5,5,55,546])
print(list(r))

def add(x, y):
    return x + y

print(reduce(add, [1,2,2,2,2,4,56,7,7,78]))

# 函数&可变参数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-90))

def calcu(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(calcu([1, 2, 3, 4, 5, 6, 9]))
print(calcu((1, 2, 3, 4, 5, 6, 9)))

def mutateCalc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(mutateCalc(1,2,3,4,5,4,4,4))

def keyCalc(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

keyCalc('Bob', 23, city='Beijing')
keyCalc('Tom', 56, gender='M', job='Engineer')


def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

def f2(a, b, c=0, * ,d, **kw):
     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

def fabfic(n):
    if n==1:
        return 1
    return n*fabfic(n-1)

print(sorted([23, 4, -12, -21, 9, 17]))

print(fabfic(9))

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())

list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

print('----------------------分割线--------------')


#装饰器
def log(func):
    def wrapper(*arg, **kw):
        print('call %s():' % func.__name__)
        return func(*arg, **kw)
    return wrapper

@log
def now():
    print('2018-4-26')

now()



class Animal(object):
    def __init__(self, name):
        self.name = name

dog = Animal('Bon')
dog.nick = 'You'

print(isinstance(dog, Animal))


class Teacher(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score is not int')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100')
        self._score = value

t = Teacher()
print(t)

# t.score = 999

print('----------------------分割线--------------')


print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

def matchResult(test):
    if re.match(r'^\d{3}\-\d{3,8}$', test):
        print('ok,hhh,match ok')
    else:
        print('failed')

matchResult('010-12345')

print('----------------------分割线--------------')

def connectMysql():
    conn = mysql.connector.connect(user='root', password='gaolong', database='yirimao_2018_4')
    cursor = conn.cursor()
    sql = 'select * from user where id = 144'
    cursor.execute(sql)
    print(cursor.fetchall())

connectMysql()

print('----------------------分割线--------------')

# def load_data(y_name='Species'):
#     CSV_COLUMN = ['SepalLength', 'SepalWidth',
#                     'PetalLength', 'PetalWidth', 'Species']
#     path = '/Users/gl/Desktop/iris_training.csv'
#     train = pd.read_csv(path, names=CSV_COLUMN, header=0)
#     train_x, train_y = train, train.pop(y_name)
#     return (train_x, train_y)

# def printColum():
#     train_x, train_y = load_data()
#     columes = []
#     for key in train_x.keys():
#         columes.append(key)
#     print(columes)
#
# printColum()


print('----------------------分割线--------------')

def testNP():
    a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])


print('----------------------分割线--------------')
# parser = argparse.ArgumentParser()
# parser.add_argument('integer', type=int, help='display an integer')
# args = parser.parse_args()

# print(args.integer)

TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
print(TRAIN_URL.split('/'))
print(TRAIN_URL.split('/')[-1])

L = list(range(100))
print(L[-10:])
print(L[-20:-10:5])
print(L[1:])
print(L[::-1])
print("hhhhh, L[:]是")
print(L[:])

rand_a = np.random.rand(3)
rand_b = np.random.randn(2, 3)
print(rand_a, rand_b)

train_x = np.linspace(-1, 1, 3)
train_y = np.random.randn(*train_x.shape)
tu = (3, 4)
print(*tu)
print(train_x, train_y, type(train_x.shape))

print('----------------------分割线--------------')
