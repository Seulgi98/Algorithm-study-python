T=int(input())
for t in range(1, T+1):
    a=list(map(int,input().split()))
    sum=0
    for i in a:
        if i%2 == 1:
            sum+=i
    print('#{} {} '.format(t, sum))