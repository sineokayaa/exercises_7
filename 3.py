n = int(input())
antnms_1 = {}
antnms_2 = {}
for i in range(n):
    str = input().split()
    antnms_1[str[0]] = str[1]
    antnms_2[str[1]] = str[0]

word = input()
if word in list(antnms_1.keys()):
    print(antnms_1.get(word, word))
else:
    print(antnms_2.get(word, word))