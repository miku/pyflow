


BORDER_WIDTH = 15

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def create_empty() -> Window:
    return Window(0, 0)


# $ stubgen example.py
#
# $ cat out/example.pyi 
# from _typeshed import Incomplete
# 
# BORDER_WIDTH: int
# 
# class Window:
#     width: Incomplete
#     height: Incomplete
#     def __init__(self, width, height) -> None: ...
# 
# def create_empty() -> Window: ...
