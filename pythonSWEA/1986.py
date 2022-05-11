T=int(input())
for t in range (1, 1+T):
    N = int(input())
    sum = 0
    for i in range(1, 1+N):
        if i % 2 == 1:
           sum += i
        else :
            sum -= i

    print('#{} {}'.format(t, sum))