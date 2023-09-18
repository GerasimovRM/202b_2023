with open("test.txt", 'r') as input_file, \
        open("test2.txt", "w") as output_file:
    numbers = list(map(lambda x: str(int(x) ** 2) + '\n', input_file.readlines()))
    output_file.writelines(numbers)
