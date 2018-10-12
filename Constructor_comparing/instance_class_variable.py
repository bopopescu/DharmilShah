
class student_data:

    subject = 'maths'


    def  __init__(self):
        self.name = name
        self.rno =  rno

        print(name)
        print(rno)




name = input('enter the name ')
rno = int(input('enter the roll no '))

s1 = student_data()
print(s1.subject)

s2 = student_data()
s2.subject = 'science'
print(s2.subject)
