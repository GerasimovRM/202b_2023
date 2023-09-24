try:
    n = int(input())
    print(1 / n)
except ValueError:
    print('Просили же, введите целое число')
except ZeroDivisionError:
    print('На нуль делить нельзя')
else:
    print('Все гуд')
finally:
    print('!!!')
