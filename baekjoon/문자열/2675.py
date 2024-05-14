T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    for char in S:
        print(char * R, end="")
    print()