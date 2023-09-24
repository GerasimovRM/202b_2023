class A:
    field = 4

    def __init__(self, k):
        self.k = k


a1 = A(10)
a2 = A(5)
print(a1.field, a2.field, id(a1.field), id(a2.field))


class B:
    pass


setattr(B, 'foo', 'bar')
print(B.foo)

