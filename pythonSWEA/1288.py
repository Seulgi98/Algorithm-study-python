T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    numCountList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    i = 0
    while(True) :
        if 0 not in numCountList :
            break
        else :
            i += 1
            num = str(N*i)
            for j in num :
                numCountList[int(j)] = 1


    print("#{} {}".format(tc, num))