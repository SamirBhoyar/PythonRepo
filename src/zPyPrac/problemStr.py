text = 'H1e2l3l4o5w6o7r8l9d'
chars = list(text)

def even(word):
    new_word = []
    for i in range(len(word)):
        if i % 2 == 0:
            new_word.append(word[i])
    return new_word

print(even(chars))

print('==============================')

result = [text[i] for i in range(len(text)) if i % 2 == 0]
print(result)
print(''.join(result))

print('==============================')

print(text[::2])