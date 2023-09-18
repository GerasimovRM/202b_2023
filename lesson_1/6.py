from random import randint
a = [randint(1, 10) for _ in range(100)]
for i, elem in enumerate(a, 100):
    print(i, elem)