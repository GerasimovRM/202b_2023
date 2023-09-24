import pickle

with open("4.pickle", "rb") as input_stream:
    lst = pickle.load(input_stream)

print(lst, type(lst), lst[0])
