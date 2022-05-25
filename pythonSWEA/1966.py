T = int(input())
for tc in range(1, 1 + T):
    n = int(input())
    arr = list(map(int, input().split()))
    sort = sorted(arr)
    res = ' '.join(map(str, sort))
    print("#{} {}".format(tc, res))
