print('Using class and objects ')


class compute:
    def rectangle(self):
        result = 5 * 5
        return result
    print('in class compute ')


c1 = compute ()
d = c1.rectangle()
print(d)


class demo:
    def test(self):
        print('In fun test')
    print('in class demo ')


d1 = demo()
d1.test ()