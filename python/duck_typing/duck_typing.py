class pycharm :
    def execute(self):
        print('compile')
        print('run')

class laptop:
    def code(self,ide):
        ide.execute()

ide = pycharm()
l1 = laptop()
l1.code(ide)