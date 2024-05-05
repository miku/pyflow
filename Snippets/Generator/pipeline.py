

numbers = (i for i in range(1, 10))
squared = (i*i for i in numbers)
filtered = (i for i in squared if i % 7 == 0)

for v in filtered:
    print(v)
