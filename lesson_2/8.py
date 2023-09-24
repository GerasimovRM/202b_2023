import pickle
from task_7 import A

with open("7.pikcle", "rb") as input_stream:
    new_a = pickle.load(input_stream)

print(new_a, new_a.arg1, new_a.arg2, type(new_a))
