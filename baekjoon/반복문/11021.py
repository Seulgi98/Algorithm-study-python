import sys

T = int(sys.stdin.readline().rstrip())
for i in range(0, T):
    line = sys.stdin.readline().rstrip()
    A, B = map(int, line.split())

    print(f"Case #{i+1}: {A+B}")