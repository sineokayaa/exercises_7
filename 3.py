n = int(input())
antnms = {}

for i in range(n):
    str = input().split()
    antnms[str[0]] = str[1]

word = input()

print(antnms.get(word, word))
