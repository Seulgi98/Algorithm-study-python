n=int(input())
a=list(map(int, input().split()))
a.sort()
print(a[int(n/2)])
