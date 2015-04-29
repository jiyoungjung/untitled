# -*- coding utf-8 -*-

__author__ = 'jyjung'

tuple = (4, 5)
list = [6, 7]

x, y = tuple
dict = {
    'name' : 'jyjung',
    'age' : '20'
}


print x
print y
print dict


with open('sample', 'rt') as f:
    data = f.read()
    print data


sum = 0
for i in range(1, 11):
    sum = sum + i

print(sum)
