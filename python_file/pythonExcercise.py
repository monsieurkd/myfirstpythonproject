import site
import struct
import os
import platform
from datetime import date
import math
import datetime
import sys
from calendar import MONDAY, Calendar, c, calendar
from re import A, sub
from secrets import choice
from site import abs_paths
from textwrap import indent
from tokenize import Number

print(sys.version_info)
print(sys.version)

# 3


now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%d-%m %H:%M:%S"))
# important to do random algorithms
# 4
'''import math

r = float(input('bán kính:  '))
S= r**2 * math.pi
print(S)
'''
# 5
'''str= input('nhập dãy: ')
list=str.split(',')
tuple= tuple(list)
print(list)
print(tuple)'''

# 7
'''
xfilename = input("Input the Filename: ")
f_extns = filename.split(".")
print(f_extns)
print ("The extension of the file is : " + repr(f_extns[-1]))
'''
# 8
exam_st_date = (11, 12, 2014)
print('The examination will start from : ' +
      repr(exam_st_date[0]) + '/' + repr(exam_st_date[1]) + '/' + repr(exam_st_date[2]))

# 9

print(abs.__doc__)

# 10
'''
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.year(y, m)) '''

# 14

f_date = date(2022, 10, 5)
s_date = date(2005, 5, 24)
day = f_date - s_date
print(day)

# 15
'''
from math import pi 
R = int(input('nhập bán kính: '))
V = 4/3*pi*R**3
print(V)'''

# 16
'''A = int(input('nhập một số: '))
chenhLech = abs(17 - A)

if A > 17:
    print(chenhLech*2)
else:
    print(chenhLech)'''


def tong_ba_so(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum + sum * 3
    return sum


print(tong_ba_so(1, 2, 3))
print(tong_ba_so(4, 4, 4))

# 19
'''chuoi = input('nhập dãy: ')
if chuoi.startswith('Is'):
    print(chuoi)
else:
    print('Is ' + chuoi)
'''
# 20
'''a = input('nhập dãy: ')
b = int(input())
if b >= 0:
    print(a*b)'''

'''b=input()
count=0
for i in b:
    if i == '4':
        count= count+1
print(count)'''

# 24

# 25


def check(so):
    a = [1, 5, 8, 3]
    if so in a:
        return True
    else:
        return False


print(check(3))
print(check(-1))
# 27


def concatenate(list):
    day = ''
    for a in list:
        day = day + repr(a)
    return day


print(concatenate([1, 5, 6, 8, 7, 5, 9]))

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527]
number1 = []
for a in numbers:
    if a % 2 == 0:
        if numbers.index(a) <= numbers.index(237):
            number1.append(a)
print(number1)

# 29

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
a = sorted(color_list_1)
b = sorted(color_list_2)
c = list()
for x in a:
    if x in b:
        c.append(x)
print(c)
d = []
for y in a:

    if y not in c:
        d.append(y)
print(d)

# 31


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


print(gcd(10, 5))

p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

print(distance)
# Write a Python program to check whether a file exists.
print(os.path.exists('Nháp.py'))
print(os.path.exists('as.txt'))
# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS
print(platform.architecture()[0])
print(struct.calcsize("P") * 8)
# Write a Python program to get OS name, platform and release information. Go to the editor
print("Name of the operating system:", os.name)
print("\nName of the OS system:", platform.system())
print("\nVersion of the operating system:", platform.release())
# Write a Python program to locate Python site-packages.
print(site.getsitepackages())

#call an external command
os.system('dir *.md')

'''
45. Write a Python program to call an external command. Go to the editor
Click me to see the sample solution

46. Write a python program to get the path and name of the file that is currently executing. Go to the editor
Click me to see the sample solution

47. Write a Python program to find out the number of CPUs using.'''


