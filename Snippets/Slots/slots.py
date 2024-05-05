class Default:

    def __init__(self):
        self.slot_0 = "zero"
        self.slot_1 = "one"


class Example:
    __slots__ = ("slot_0", "slot_1")
    
    def __init__(self):
        self.slot_0 = "zero"
        self.slot_1 = "one"


# Can set attributes on objects
d1 = Default()
print(d1.slot_0)
d1.slot_2 = "ok"
print(d1.slot_2)

# Cannot set additional attributes
x1 = Example()
print(x1.slot_0)
print(x1.slot_1)
# x1.slot_2 = "fail" # AttributeError: 'Example' object has no attribute 'slot_2'
# print(x1.slot_2)

