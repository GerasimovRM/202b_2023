with open("test.txt", 'r') as input_file, \
        open("test2.txt", "w") as output_file:
    for line in map(int, input_file):
        number = line
        number **= 2
        output_file.write(str(number) + "\n")
