words = [input() for _ in range(5)]

def read_vertical(words):
    max_length = max(len(word) for word in words)
    result = []

    for i in range(max_length):
        for word in words:
            if i < len(word):
                result.append(word[i])

    return ''.join(result)



print(read_vertical(words))
