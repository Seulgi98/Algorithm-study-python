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
        for j in range (N): # N의 길이가 더 짧으므로 N의 전체 길이에 맞추어 인덱스가 들어감
            temp += A[j] * B[j+i]
        if temp > maxSum: # temp가 더 크면 무조건 max로 담아준다
            maxSum = temp

    print('#{} {}'.format(tc, maxSum))
