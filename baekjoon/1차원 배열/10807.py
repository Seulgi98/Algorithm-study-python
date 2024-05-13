N = int(input())
elements = input().split()
array = [int(i) for i in elements]

v = int(input())
count_element = array.count(v)

print(count_element)