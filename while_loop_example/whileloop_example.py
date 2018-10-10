import sys

print('using While Loop Example')

i=1 #intializaton
j=1
while i<5: #condition
    print('*',end='')
    j=1
    while j<=4:
        print('*',end='')
        j=j+1
    i=i+1#iteration
    print()

k=1
while k<=100:
    if(k%3!=0) and (k%5!=0):
        print(k)
    k=k+1