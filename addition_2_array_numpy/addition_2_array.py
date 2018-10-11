from numpy import *

arr11 = array([1, 2, 3, 4])
arr12 = array([1, 2, 3, 4])

sum = 0
for i in arr11:
    for j in arr12:
        sum = arr11 + arr12

print ('sum of 2 array', sum)
