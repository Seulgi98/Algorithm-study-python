T = int(input())
for t in range(1, T + 1):
    num = int(input())
    arr = list(map(int, input().split()))
    arr = arr[::-1]
    max = arr[0]
    res = 0
    for i in range(1, len(arr)):
        if max > arr[i]:
            res += max - arr[i]
        else:
            max = arr[i]
    print("#{} {}".format(t, res))