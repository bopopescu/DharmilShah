class A:
    def show(self):
        print(' In A ')

class B(A):
    pass
   # def show(self):                # if un-comment this method that In B will display
    #    print(' In B ')




a1 = A()
a1.show()
b1 = B()
b1.show()

class C:
    def show(self):
        print('In c')

class D(C):
    def show(self):
        print('In D')


c1 = C()
c1.show()
d1 = D()
d1.show()