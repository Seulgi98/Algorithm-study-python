N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))
    print('A : ', A)

for _ in range(N):
    B.append(list(map(int, input().split())))
    print('B : ', B)


C = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]

for row in C:
    print(' '.join(map(str, row)))
