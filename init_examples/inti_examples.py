
class demo:
    def __init__(self, _val1, _val2):
            self.val1 = _val1
            self.val2 = _val2


    def ma(self):
        result = self.val1 + self.val2
        print(result)

val1 = int(input('enter the value 1'))
val2 = int(input('e2nter the value 2'))

d2 = demo(val1,val2)
d2.ma()
