import sys

a=int(input('enter a nummber'))
b=int(input('etner a number'))

if(a>0):
    print('number is postive')
else:
    print('number is negative')


c=int(input('enter a number'))
if(a>b)and(a>c):
    print('a is max')
elif(b>a)and(b>c):
    print('b is max')
else:
    print('c is max')

