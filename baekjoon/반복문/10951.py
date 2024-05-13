import sys

while True:
    try:
        line = sys.stdin.readline().strip()
        A, B = map(int, line.split())
        print(A + B)
    except:
        break