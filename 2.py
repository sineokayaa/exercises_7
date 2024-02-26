n = int(input())
ru_eng = {}
for i in range(n):
    text = input().split()
    ru_eng[text[0]] = text[1]

sentence = input().split()

translation = ''
for i in range(len(sentence)):
    if sentence[i] in list(ru_eng.keys()):
        translation += ru_eng[sentence[i]] + ' '
    else:
        translation += sentence[i] + ' '

print(translation)
