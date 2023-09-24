def decorator_gen(n):
    def decorator(old_func):
        def new_func(*args, **kwargs):
            print("начали выполнение функции")
            result = old_func(*args, **kwargs)
            print("закончили выполнение функции")
            return result + n
        return new_func
    return decorator


def class_gen_decorator(path):
    def class_decorator(cls):
        class NewClass(cls):
            def example(self):
                return 10
        return NewClass
    return class_decorator


@class_gen_decorator("temp.json")
class A:
    def __init__(self, field):
        self.field = field


@decorator_gen(3)
def f(a, b):
    return a + b


# f = decorator(f)

print(f(3, 5))
