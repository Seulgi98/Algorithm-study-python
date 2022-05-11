T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    listA = [0]*10
    # print('listA',listA)
    i = 0
    while(True) :
        if 0 not in listA :
            break
        else :
            i += 1
            num = str(N*i)
            for j in range(len(num)) :
                # print('i', i, 'j', j)
                listA[int(num[j])] = 1
                # print('listA', listA)

    print("#{} {}".format(tc, num))