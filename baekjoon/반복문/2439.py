import sys

N = int(sys.stdin.readline().strip())
space = " "
star = "*"

for i in range(1, 1+N):
    print(space*(N-i)+star*i)