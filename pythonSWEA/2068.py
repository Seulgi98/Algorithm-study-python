T = int(input())
for t in range(1, T + 1):
    a = list(map(int, input().split()))
    arrMin = int(0)
    for i in a:
        if i >= arrMin:
            arrMin = i
    print("#{} {}".format(t, arrMin))