h, m = map(int, input().split())
minutes = int(input())

if m + minutes >= 60:
    add_hour = int(minutes / 60)
    add_min = (minutes % 60)

    h += add_hour
    m += add_min

    if m == 60:
        m = 0
        h += 1
    elif m > 60:
        m -= 60
        h += 1
    if h >= 24:
        h -= 24
else:
    m += minutes

print(h, m)