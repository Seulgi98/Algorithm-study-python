array = [[0] * 101 for _ in range(101)]
N = int(input())
for _ in range(N):
    x, y = list(map(int, input().split()))

    for row in range(x, x + 10):
        for col in range(y, y + 10):
            array[row][col] = 1

res = 0

for i in array:
    res += i.count(1)
print(res)
