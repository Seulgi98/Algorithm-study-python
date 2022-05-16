T=int(input())

for tc in range(1, 1+T):
    m1, d1, m2, d2 = map(int, input().split())
    date = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    res = 0
    for i in range(m1, m2) :
        print(0)
        if m1 == i :
            print('i', i)
            print('date', date[i])
            res += date[i] - d1 + 1
            print('if res', res)
            print(1)
        else :
            res += date[i]
            print('else res', res)
            print(2)
    print(3)
    res += d2
    print(4)
    print('res', res)
    print("#{} {}".format(tc, res))