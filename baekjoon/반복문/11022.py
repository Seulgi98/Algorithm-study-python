import sys

T = int(sys.stdin.readline().rstrip())

for i in range(1, T+1):
    line = sys.stdin.readline().strip()
    A, B = map(int, line.split())

    print(f"Case #{i}: {A} + {B} = {A+B}")