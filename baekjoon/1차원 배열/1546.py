N = int(input())
score = list(map(int, input().split()))

max_score = max(score)
sum = 0

for i in score:
    sum += i/max_score * 100

print(sum/N)
