words = input().split()
ness = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
result = ''

for i, word in enumerate(words):
    if word in ness and i != 0:
        continue

    result += word[0].upper()

print(result)
