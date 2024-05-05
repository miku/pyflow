class Sample:

    def __getitem__(self, key):
        return "42" # raise KeyError

s = Sample()
print(s["hi"])
print(s["hello"])

s["hi"] = 43