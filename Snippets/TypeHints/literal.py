from typing import Literal

def hello(name: Literal["Alice", "Bob"]):
    print(f"hello {name}")
    
    
hello("Alice")
hello("Anne")

# TypeHints/literal.py:8: error: Argument 1 to "hello" has incompatible type "Literal['Anne']"; expected "Literal['Alice', 'Bob']"
# Found 1 error in 1 file (checked 1 source file)
