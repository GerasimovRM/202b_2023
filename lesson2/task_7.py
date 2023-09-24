import pickle


class A:
    def __init__(self, arg1, agr2):
        self.arg1 = arg1
        self.arg2 = agr2


a = A({"asdas": [12, 123, True], "sdfds": [2345, True, None], "hsdl": (True, False)},
      [[1, 2, 3], [4, 5, 6]])

with open("7.pikcle", "wb") as output_stream:
    pickle.dump(a, output_stream)

with open("7.pikcle", "rb") as input_stream:
    new_a = pickle.load(input_stream)

print(new_a, new_a.arg1, new_a.arg2, type(new_a))