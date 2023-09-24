import pickle

lst = [1, 2, 3, True]

with open("4.pickle", 'wb') as output_stream:
    pickle.dump(lst, output_stream)
