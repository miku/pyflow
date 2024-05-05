from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def  __init__(self, k : T):
        self.k = k
        
    def __repr__(self):
        return f'{self.k} of type {type(self.k)}'
    

node = Node(int)
print(node)

node = Node(123)
print(node)
