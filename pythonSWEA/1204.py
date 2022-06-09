T = int(input())
for t in range(1, T + 1):
    n = input()
    grade = list(map(int, input().split()))  # 각 값은 100이하, 개수는 1000개, 점수
    cnt = [0] * 101  # 1~100점까지의 개수
    max = 0  # 많이 나온 개수
    res = 0  # 최빈수의 점수

    for i in range(len(grade)):
        cnt[grade[i]] += 1

    for j in range(1, len(cnt)):
        if max <= cnt[j]:
            max = cnt[j]
            res = j

    print('#{} {}'.format(t, res))
