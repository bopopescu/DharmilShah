class student:
    def enterdata(self):
        name = input('enter the name')
        rno = int(input('enter the roll no'))
        self.name = name
        self.rno = rno


class subject(student):
    def sub(self):
        sub = input('enter the subject')
        self.sub = sub
class showdata(subject):
    def showdata(self):
        print('name :',self.name)
        print('Rollno :', self.rno)
        print('Subject :', self.sub)

sd = showdata()
sd.enterdata()
sd.sub()
sd.showdata()