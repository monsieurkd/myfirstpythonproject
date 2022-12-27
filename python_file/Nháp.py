from tkinter import Y
from xml.dom import EMPTY_NAMESPACE


print("hello world0")

# 10/2/22
try:
    txt= 'testing try and except'
    txt0 = int(txt)
    print('we start simple')
except:
    print('sô its easy')

Y='chưa hiểu base' #các hệ lục thập nhị đều hoạt động giống nhau trừ hệ 16 với từ 10- 15 lần lượt là A-F 
x = '0b1110'
b=int(x, 16)
print(b)

#11/2/22
for a in range (0,b):
    if a < 4:
        continue
    if a ==5:
        break
    print(a)

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

c=None
if c == None:
    print('none is the type that indicate empty')
else :
    print('you suck')

x = 'banana'
y= 'apple and banana '
if y > x:
    print('y>x')
elif y < x:
    print('y<x')

print(dir(x))
print(y.lstrip() + y)
print(y.startswith('a'))


#4/10/22
''' from pathlib import Path

p = Path('IT').with_name('testfile')
with p.open('r') as f:
    print(f.read()) '''

'''with open('as.txt', encoding='utf8') as f:
    for line in f:
        print(f.readline())'''

'''try: 
    x= int(input())
    for a in range(x):
        print(a)
except:
    print('x=-1')'''

#else and finally 
#continue skip the conditions and then continue the looping
str= 'sfdf.45'
print(str.find('.'))

dict = {'12':2, 'aaskjd':3, 'asfk':5}
print(sorted(dict.items()))

