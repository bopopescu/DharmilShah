class stu:
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2

    def __add__(self, other):
        a1 = self.a1 + other.a1
        a2 = self.a2 + other.a2
        s3 = stu(a1,a2)

        return s3

    def __gt__(self, other):
        g1 = self.a1 + other.a1
        g2 = self.a2 + other.a2
        if g1 > g2:
            return True
        else:
            return False



s1 = stu(10,20)
s2 = stu(20,30)
s3 = s1 + s2
print(s3.a1)

if s1 > s2:
    print('g1 is greater')
else :
    print('g2 is greater')

