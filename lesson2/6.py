import pickle


lst = [1, 2, 3, True]

s = pickle.dumps(lst)
new_lst = pickle.loads(s)
print(new_lst)