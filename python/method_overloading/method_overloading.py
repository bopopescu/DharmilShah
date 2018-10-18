class  moverload:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2



    def sum(self,a=None, b=None, c=None):
        result = 0

        if a!= None and b!= None and c!= None :
            result = a+ b+ c

        elif a!= None and  b!= None :
            result = a + b
        else:
            result = a * a
        return result

m1 = moverload(1, 2)
print(m1.sum(10, 20 ))
