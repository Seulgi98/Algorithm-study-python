N, X = map(int, input().split())
array = list(map(int, input().split()))

result = [num for num in array if num < X]
print(*result)