class stu:
    university = 'abc'

    def __init__(self,a1,a2,a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def avg(self):
        return (self.a1 + self.a2 + self.a3)/3

    @classmethod
    def info(cls): # cls is used to use the class variable uni so the method becomes class method
        return cls.university

    @staticmethod
    def get():
        print('use of static method')

s1 = stu(12,1,4)
#s2 = stu(34,56,1)
print(s1.avg())
print(s1.info())
stu.get()
print(s1.get())