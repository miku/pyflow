

class Backend1:
    
    def op(self):
        return 20
    

class Backend2:
    
    def op(self):
        return 11



class Facade:
    
    def __init__(self, b1=None, b2=None):
        self.backend1 = b1
        self.backend2 = b2
        
    def answer(self):
        return self.backend1.op() + self.backend2.op() * 2
    

b1 = Backend1()
b2 = Backend2()
f = Facade(b1=b1, b2=b2)
print(f.answer())
        
        