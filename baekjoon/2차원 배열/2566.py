N = 9
matrix = []
max_value = -1
max_location = [0, 0]

for _ in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if max_value < matrix[i][j]:
            max_value = matrix[i][j]
            max_location = [i + 1, j + 1]

print(max_value)
print(max_location[0], max_location[1])
