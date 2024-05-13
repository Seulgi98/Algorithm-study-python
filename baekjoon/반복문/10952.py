import sys

line = sys.stdin.readline().strip()
A, B = map(int, line.split())

while A != 0 and B != 0:
    print(A+B)
    line = sys.stdin.readline().strip()
    A, B = map(int, line.split())
