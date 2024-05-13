array = []

for i in range(0, 9):
    element = int(input())
    array.append(element)

max_value = max(array)
max_index = array.index(max_value)

print(max_value)
print(max_index + 1)