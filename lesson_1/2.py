with open("test.txt", "r") as f:
    a = f.read(2)
    # print(sum(map(int, a.split())))
    print(a)
    b = f.read(3)
    print(b)

