T = int(input())
dict={
    '01':31,
    '02':28,
    '03':31,
    '04':30,
    '05':31,
    '06':30,
    '07':31,
    '08':31,
    '09':30,
    '10':31,
    '11':30,
    '12':31
}

for t in range(1, T + 1):
    date = input()
    value = ""
    # print("#{}".format(t), end=' ')
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]

    if int(month) > 12 or int(month) <= 0 :
        value = -1
        # print(-1)

    elif dict[month] < int(day) or int(day) <= 0 :
        value = -1
        # print(-1)

    else :
        value = year+"/"+month+"/"+day
        # print(year+"/"+month+"/"+day)

    print("#{} {}".format(t, value))
