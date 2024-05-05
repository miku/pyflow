from typing import Union

def fetch(k:int = 0) -> Union[int, str]:
    if k == 0:
        return 0
    else:
        return "nonzero"
    
    
print(fetch(k=1))
print(fetch(k=0))