import sys

old_sys_stdin = sys.stdin
with open("input.txt", "r") as input_file:
    sys.stdin = input_file

    a, b = int(input()), int(input())
    print(a + b)
sys.stdin = old_sys_stdin
