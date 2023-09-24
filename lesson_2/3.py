def func(a, b):
    if b == 0:
        raise ZeroDivisionError("Аргумент b не может быть равен 0!!!")
    return a / b


func(3, 0)
