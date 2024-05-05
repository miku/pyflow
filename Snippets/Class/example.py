class A:

    i = 0

    def __new__(cls):
        cls.i += 1
        return super(A, cls).__new__(cls)
    
    def __init__(self):
        print("initialize object")

    def foo(self):
        return "i is {}".format(self.i)

a = A()
b = A()
c = A()

print(A.i)
print(a.foo())