from numpy import *

a1 = array ([
                [1, 2, 3, 4, 5, 6],
                [4, 5, 6, 7, 8, 9]

            ])
print(a1)
print('data type of the array ', a1.dtype)
print('dimension of the array is : ', a1.ndim )
print('represent row and column of the md-array ', a1.shape)
print('size of the array is ', a1.size)

print()
a2 = a1.flatten()
print(' convert md-array to 1d-array ', a2)

a3 = a2.reshape(3,4) # 1st arg represent number of rows and 2nd arg represent the number of columns
print('convert 1d array to 3d array ')
print(a3)
print()
print('represent the array in md-array ')
a4 = a3.reshape(2, 2, 3) # 1st argu is no of array 2nd arg contains 2 2d array and 3rd argu represent no of cols per array
print(a4)
print()

print('matrix representation')
m = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
print(m)

print('diagonal matrix is')
print(diagonal(m))
print('min element of matrix is : ', m.min())
print('min element of matrix is : ', m.max())
m3 = m + m1
print('addition of 2 matrix : ')
print(m3)
m4 = m * m1
print('multiplication of 2 matrix :')
print(m4)


