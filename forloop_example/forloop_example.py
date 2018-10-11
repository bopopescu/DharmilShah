import sys
import math
print('using For Loop example')

# print('for loop using list')
# d=['hello','hi','welcome']
#
# for i in d:
#     print(i)
#
# print('for loop to print single character of string')
# d1='WELCOME'
# for j in d1:
#     print(j)
#
# for k in range(11):
#     print(k)

#for i in range(1,501):
 #   y=i*i
  #  if(y<501):
   #     print(y)

for i in range(4):
    for j in range(4 - i):
        print(j + i + 1, end=" ")
    print()
