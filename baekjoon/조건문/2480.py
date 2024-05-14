dice = list(map(int, input().split()))
prize = 0
max_die = max(dice)

if dice[0] == dice[1] == dice[2]:
    prize = 10000 + dice[0] * 1000
elif dice[0] != dice[1] and dice[1] != dice[2] and dice[0] != dice[1]:
    prize = 100 * max_die
else:
    if dice[0] == dice[1]:
        prize = 1000 + dice[0] * 100
    elif dice[1] == dice[2]:
        prize = 1000 + dice[1] * 100
    elif dice[0] == dice[2]:
        prize = 1000 + dice[0] * 100

print(prize)
