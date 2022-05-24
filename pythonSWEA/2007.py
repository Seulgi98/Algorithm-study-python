T = int(input())
for tc in range(1, T + 1):
    text = input()
    for i in range(1, 10):  # 마디의 최대 길이가 10이므로
        if text[:i] == text[i:i * 2]:
            print('#{} {}'.format(tc, i))
            break
