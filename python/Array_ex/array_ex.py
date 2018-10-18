from array import *

print('using Array Examples')
arr = array('i',[1,2,1,4])
print(arr)

print(arr.buffer_info())

print('counts particular number occur in the array')
print(arr.count(1))
print('append the item at the end of the array')
arr.append(5)
print(arr)
print('reverse the entire array')
arr.reverse()
print(arr)

print('prints entire array using loop')
for i in arr :
    print(i)

a1=array('u',['a','b','c','d'])
for j in a1:
    print(j)

print('using typecode ')
a2=array(a1.typecode,(a for a in a1))
print(a2)


