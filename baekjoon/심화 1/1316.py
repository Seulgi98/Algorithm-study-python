N = int(input())
word_list = [input().strip() for _ in range(N)]

def check_word(word):
    prev = ''
    prev_chars = set()
    for char in word:
        if char != prev:
            if char in prev_chars:
                return False
            prev_chars.add(char)
            prev = char
    return True

def count_group_word(words):
    count = 0
    for word in words:
        if check_word(word):
            count += 1
    return count

result = count_group_word(word_list)
print(result)