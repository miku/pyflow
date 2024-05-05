class A:

    def __init__(self):
        self.a = "42"
    
    def __str__(self):
        return "<A a={}>".format(self.a) # <A a=42>
    
    def __len__(self):
        return 42


a = A()
print(a) # <__main__.A object at 0x7f7f280930d0>

print(len(a))