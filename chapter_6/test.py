class Test:
    def __init__(self):
        print('初始化')


print('start')
def x(a=Test()):
    print('函数内部')


x()
