class Str(str):

    def __eq__(self, other):
        if not isinstance(other, str):
            raise TypeError
        return self.lower() == other.lower()



a = "Hello"
b = "hello"

print(a == b)
print(Str(a) == Str(b))