from functools import *

print('Lamda Filter Map Reduce')

nums = [2, 3,  4, 1, 4, 6, 7, 3, 4, 1]

primee = list(filter(lambda n : n%2!=0, nums))
print(primee)

multi = list(map(lambda n : n * n, primee))
print(multi)

redu = reduce(lambda a,b : a +b, multi)
print(redu)
print('')
n1 = [10,23,12,4,68,43]
big = list(filter(lambda n : n<30,n1))
print(big)

increment = list(map(lambda n : n* n* n, big))
print(big)

sum = reduce(lambda a,b: a+b, big)
print(sum)



