from _typeshed import Incomplete

BORDER_WIDTH: int

class Window:
    width: Incomplete
    height: Incomplete
    def __init__(self, width, height) -> None: ...

def create_empty() -> Window: ...
