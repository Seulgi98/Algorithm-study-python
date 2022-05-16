T = int(input())
for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)] #리스트 내포 방식을 활용한 입력
    ans = 0

    for i in range(N):
        cnt = 0
        # 행을 검사
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                # 벽을 만났을 때 그동안 쌇아온 cnt 값이 k이면 들어갈 수 있다.
                if cnt == K:
                    ans += 1
                cnt = 0

        # 열을 검사
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0
    print("#{} {}".format(tc, ans))