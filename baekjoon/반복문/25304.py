X = int(input())
N = int(input())
total_sum = 0

for i in range(1, N+1):
    a, b = map(int, input().split())
    total_sum += a * b

if X == total_sum:
    print("Yes")
else:
    print("No")