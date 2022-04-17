T=int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    print("#{} {} {}".format(t, int(a/b), int(a%b)))