T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M: #M이 큰값이 되도록 순서 변경
        N, M = M, N
        A, B = B, A
    maxSum = 0

    for i in range (M-N+1):
        temp = 0
        for j in range (N):
            temp += A[j] * B[j+i]
        if temp > maxSum:
            maxSum = temp

    print('#{} {}'.format(tc, maxSum))
