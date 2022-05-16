months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, int(input())+1):
    m1, d1, m2, d2 = map(int, input().split())
    ans = 0

    # 같은 달에 위치할 경우
    if m1 == m2:
        ans = d2 - d1 + 1

    else:
        # 시작하는 달
        ans = months[m1] - d1 + 1
        # 중간에 있는 달
        for i in range(m1 + 1, m2):
            ans += months[i]
        # 마지막 달
        ans += d2
    print('#{} {}'.format(tc, ans))