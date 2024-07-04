N = 9
matrix = []
max_value = 0
max_location = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if max_value < matrix[i][j]:
            max_value = matrix[i][j]
            max_location = [i + 1, j + 1]

print(max_value)
print(' '.join(map(str, max_location)))
