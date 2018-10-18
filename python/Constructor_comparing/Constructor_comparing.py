class sdata:
    def __init__(self):
        self.val1 = val1
        self.val2 = val2


    def display(self):
        print('name :', self.val1)
        print('subject :', self.val2)


    def compare(self, other):
        if self.val2 == other.val2:
            return True
        else:
            return False

val1 = input('enter the name :')
val2 = input('enter the subject :')


sd1 = sdata()
sd1.val2 = 'kk'
sd2 = sdata()

if sd1.compare(sd2):
    print("same")
else:
    print("different")