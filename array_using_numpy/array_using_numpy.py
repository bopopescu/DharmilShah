from numpy import *

arr = array([1, 2, 3, 3.4, 5, 6, 7, 7])
print(arr)

print('using linspace function ')
arr1 = linspace(1, 5, 10)  # here 1st para represent starting value, 2nd value represent end value, 3rd represent no of breaks in the given start and end value
print(arr1)

print('using arange funtion')
arr2 = arange(1, 5, 3)  # here 3rd argu represent number of skips/increment from current value to reach the end position
print(arr2)

print('using logspace function')
arr3 = logspace(1, 5, 3)  # here 3rd argu represent the log so the entire range will be divide in form of log
print(arr3)
print('%2f' % arr3[0])

print('using zeros function')
arr4 = zeros(5)  # zeros is used to create an array of zeroes
print(arr4)

print('using ones function')
arr5 = ones(5)  # here ones is used to create an array of ones
arr6 = ones(5, int)
print(arr5)
print(arr6)

print('addition of 2 array')
arr7 = array([1, 2, 4, 5, 6])
arr8 = array([3, 7, 8, 9, 10])
arr9 = arr7+arr8
print(arr9)

print('cos of array', cos(arr9))
print('sin of array', sin(arr9))
print('min value of array', min(arr9))
print('max value of array', max(arr9))
print('sorting of array', sort(arr9))
print('concatenation of array,', concatenate([arr7,arr8]))

print('copying of array')
arr10 = arr9.copy()
print(arr10)


arr11 = array([1, 2, 3, 4])
arr12 = array([1, 2, 3, 4])
sum = 0
for i in arr11:
    for j in arr12:
        sum = arr11 + arr12

print ('sum of 2 array', sum)

















