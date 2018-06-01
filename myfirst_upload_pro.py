import time

class myclass(object):
    def __init__(self, name):
        self.name = name
    def func(self):
        print(time.time())
        print('hello the future president:', self.name)


if __name__ == '__main__':
    my = myclass('lgh')
    my.func()