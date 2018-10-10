import sys


print('using input value from user')
a = input('enter the value :')
b = input('enter the value :')
print('the input function take arguments in the string ')
print(type(a))
print(type(b))

x = int(input('enter the value  : '))
y = float(input('enter the value : '))
z = x+y
print(z)

print('to print only single character ')
ch = input('enter a character')
print(ch[0])

ch1 = input('enter a character')[0]
print(ch1)

print('to evaluate particular expressign then used eval function')
res = eval(input('enter the expression'))
print(res)

# will only work in cmd
#print('using command line arguments')
#a1=int(sys.argv[1])
#a2=int(sys.argv[2])
#a3=a1+a2
#print(a3)