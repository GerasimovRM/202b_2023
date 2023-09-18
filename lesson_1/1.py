with open("test.txt", "r") as f:
    for line in map(str.strip, f.readlines()):
        print(line)


