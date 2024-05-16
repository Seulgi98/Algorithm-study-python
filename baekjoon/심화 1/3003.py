# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
find_chess = list(map(int, input().split()))
need_chess = [1, 1, 2, 2, 2, 8]
result = []

for i in range(0, 6):
    if find_chess[i] != need_chess[i]:
        result.append(need_chess[i] - find_chess[i])
    else:
        need_chess[i] = 0
        result.append(need_chess[i])

print(*result)