class student:

    def __init__(self):
        print('in A')

    def enterdata(self):
        name = input('enter the name')
        rno = int(input('enter the roll no'))
        self.name = name
        self.rno = rno


class subject(student):

    def __init__(self):
        print('in B')

    def sub(self):
        sub = input('enter the subject')
        self.sub = sub

class showdata(subject):

    def __init__(self):
        print('in C')
        super().__init__()
    def showdata(self):
        print('name :',self.name)
        print('Rollno :', self.rno)
        print('Subject :', self.sub)

sd = showdata()
sd.enterdata()
sd.sub()
sd.showdata()