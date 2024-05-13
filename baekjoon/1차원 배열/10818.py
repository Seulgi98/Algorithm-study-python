N = int(input())
array = list(map(int, input().split()))

array.sort()
print(array[0], array[N-1])