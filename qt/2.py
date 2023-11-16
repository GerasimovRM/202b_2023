import sys


print(sys.argv)
a, b = map(int, sys.argv[1:3])
print(a + b)