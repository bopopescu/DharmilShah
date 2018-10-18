from array import *

arr = array('i',[])
n = int(input('enter the length of the array'))

for i in range(n):
    x=int(input('enter the value for array'))
    arr.append(x)
print (arr)

print('reversing the array')
arr.reverse()
print(arr)

print('Popping elements of the array')
arr.pop()
print(arr)

arr.insert(3,10)
print(arr)