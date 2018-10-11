print('using Functions ')

def  demo():
    print('hello')

def add(x, y):
    z = x+ y
    print('addition : ' ,z)

def sub(x, y):
    z = x -y
    w = x * y
    return z,w

def multiarg(a, *b):  # *b represent multi arguments which can accept many arg for b and for calculations used loops. data in b is tuple
    c =a
    for i in b:
        c = c + i
    print(c)

def mult1(*b):  # this also works which is known as variable line arguments. data in b is tuple
    c = 0
    for i in b:
        c = c + i
    print(c)
demo()
add(1, 2)
subtract_Result, sub_result2  = sub(2, 3)

print(subtract_Result, sub_result2 )
multiarg(3,1,2,3,4)
mult1(3,1,2,3,4)


def pdata(name, **data): # ** represent keyword arguments
    print(name)
    print(data)

pdata('abc',age=14, city='ahm', mob=213454)

def data1(name, **data):   # ** represent keyword arguments using loops
    print(name)
    for i,j in data.items():
        print(i, j)

data1  ('xyz', age=14, city='ahm', mob=213454)






