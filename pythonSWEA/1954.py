T = int(input())
# row, col 인덱스로 탐색할 수 있게 방향 설정 (달팽이 방향이니까 우->하->좌->상)
dr = [0, 1, 0, -1] # 순서대로 인덱스 0, 1, 2, 3 , dist의 숫자에 따라서 인덱스 번호가 바뀐다
dc = [1, 0, -1, 0] # 순서대로 인덱스 0, 1, 2, 3 , dist의 숫자에 따라서 인덱스 번호가 바뀐다

for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    # 초기 위치 & 회전방향 설정
    r, c = 0, 0
    dist = 0  # 0:우, 1:하, 2:좌, 3:상

    for n in range(1, N*N + 1):
        snail[r][c] = n
        r += dr[dist]
        c += dc[dist]

        # 범위를 벗어나거나 0이 아닌 다른 값이 이미 있다면, dist 방향 체인지
        # 근데 이런 경우라면 요소 인덱스를 다시 원위치시켜줘야하므로 빼줘야함
        # 그런다음 dist의 방향을 바꾸고, 방향 바꿨으면 다시 움직일 수 있도록 행렬 인덱스 업데이트
        if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0:
            # 실행취소
            r -= dr[dist]
            c -= dc[dist]
             # dist는 % 4를 하는 이유는 dist가 계속 +1되는데 이걸 안해주면 0123, 4567, ... 이런식으로 숫자 커지므로 0123으로만 접근하기 위해서 나머지를 사용
            dist = (dist + 1) % 4 # 방향 변경 (이때 dr, dc 인덱스 번호가 바뀜 , 0 -> 1번, 1->2번....)
            #  다시 gogo
            r += dr[dist]
            c += dc[dist]


    print("#{}".format(tc))
    for row in snail:
        # print('snail', snail)
        print(*row)
    print()