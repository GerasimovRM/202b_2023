import pickle


lst = [1, 2, 3, True]

with open("3_out.txt", "w") as output_file:
    print(lst, file=output_file)

with open("3_out.txt", "r") as input_file:
    st = input_file.read().strip()
    print(st)
    lst = list(st)
    print(lst)
