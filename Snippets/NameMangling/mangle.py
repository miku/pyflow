class A:
    def __init__(self):
        self.name = "any"
        self.lang = "python"

class M:
    def __init__(self):
        self.__name = "any"
        self.__lang = "python"

class B(A):
    def hello(self):
        print(self.name)

class C(M):
    def hello(self):
        print(self.name)

b = B()
c = C()

b.hello()
# c.hello() # AttributeError

