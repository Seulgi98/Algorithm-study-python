N, X = map(int, input().split())
A = list(map(int, input().split()))

result = [num for num in A if num < X]
print(*result)