from array import *

print('taking input values from user for array')

arr = array('i',[])

n = int(input('enter the length for the array '))

for i in range(n):
    print('enter the index value for location ', i)
    x = int(input('enter the value for the array '))
    arr.append(x)
print(arr)

val = int(input('enter the value you want to search'))
counter=0
for j in arr:
    if j==val:
        print('value searched',j)

    counter = counter + 1

print('index of searched value',arr.index((val)))