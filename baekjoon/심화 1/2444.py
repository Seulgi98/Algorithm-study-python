T = int(input())

for i in range(1, 2 * T):
    if i <= T:
        print(" " * (T - i) + "*" * (2 * i - 1))
    else:
        print(" " * (i - T) + "*" * (2 * (2 * T - i) - 1))
