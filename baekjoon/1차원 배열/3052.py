nums = []
remainder = []

for _ in range(10):
    num = int(input())
    nums.append(num)

for i in nums:
    remainder.append(i%42)

cnt = len(set(remainder))

print(cnt)
