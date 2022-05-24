T=int(input())
for t in range (1, 1+T):
    N=int(input())
    speed = 0
    d = 0
    for tc in range(N):
        command = list(map(int, input().split()))
        if command[0] == 0:
            speed = speed
        elif command[0] == 1:
            speed += command[1]
        elif command[0] == 2:
            speed -= command[1]
            if speed < 0:
                speed = 0

        d += speed
    print('#{} {}'.format(t, d))