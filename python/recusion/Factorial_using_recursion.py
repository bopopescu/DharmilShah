import sys

sys.setrecursionlimit(500) # default recursion limit is 1000. here we are setting that limit to 500 . we can also set for >1000 also

print('Recursion example')

def fact(x):
    if x == 0 :
        return 1
    else:
       return  x * fact(x -1 )


n = int(input('enter the value you want to find factorial '))
result= fact(n)
print(result)