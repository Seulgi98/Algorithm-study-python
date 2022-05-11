T=int(input())
for tc in range(1, 1+T):
    P, Q, R, S, W = map(int, input().split())
    A = W * P
    if (W > R):
        B = Q + S*(W-R)
    else :
        B = Q

    if A > B:
        print('#{} {}'.format(tc, B))
    else:
        print('#{} {}'.format(tc, A))
