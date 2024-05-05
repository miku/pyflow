

values = ("a", "b", "a", "c", "d")
unique = []

for v in values:
    if v in unique:
        continue
    unique.append(v)

print(unique)
