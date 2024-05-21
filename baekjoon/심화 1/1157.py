A = input()
word = A.lower()
alpha = {}

for char in word:
    if char in alpha:
        alpha[char] += 1
        print(alpha)
    else:
        alpha[char] = 1
        print(alpha)

max_count = 0
max_char = ''
result = False

for char, count in alpha.items():
    if count > max_count:
        max_count = count
        max_char = char
        result = False
    elif count == max_count:
        result = True

if result:
    print('?')
else:
    print(max_char.upper())