words = []
for _ in range(5):
    words.append(list(input()))
result = ''
for i in range(15):
    for j in range(5):
        if len(words[j]) - 1 < i:
            continue
        result += words[j][i]

print(result)
