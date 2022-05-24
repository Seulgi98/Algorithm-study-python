T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = [input().split() for _ in range(n)]

    # 90 도 회전
    arr_90 = []
    for j in range(n):
        tmp = []
        for i in range(n):
            tmp.append(arr[i][j])
            # print('tmp', tmp)

        tmp.reverse()
        # print('tmp reverse', tmp)
        arr_90.append(tmp)

    # 180 도 회전
    arr_180 = []
    for j in range(n):
        tmp = []
        for i in range(n):
            tmp.append(arr_90[i][j])

        tmp.reverse()
        arr_180.append(tmp)

    # 270 도 회전
    arr_270 = []
    for j in range(n):
        tmp = []
        for i in range(n):
            tmp.append(arr_180[i][j])

        tmp.reverse()
        arr_270.append(tmp)

    print('#{}'.format(tc))
    for i in range(n):
        print(''.join(list(map(str, arr_90[i]))), ''.join(list(map(str, arr_180[i]))), ''.join(list(map(str, arr_270[i]))))