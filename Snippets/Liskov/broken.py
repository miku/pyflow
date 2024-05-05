class CustomString(str):
    """
    A custom string class that would break Liskov substitution principle.
    """
    def __len__(self):
        """
        A this point, we change the behaviour.
        """
        return 42



s = "Hello"
t = CustomString(s)

print(len(s))
print(len(t))

def underline(s):
    return s + "\n" + "-" * len(s)


# print(underline(s))
# print(underline(t))

# Hello
# -----
# Hello
# ------------------------------------------
