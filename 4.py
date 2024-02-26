n = int(input())
pairs = {}

for i in range(n):
    pair = input().split()
    pairs[pair[0]] = pair[1:]

item = input()
for i in range(len(list(pairs.values()))):
    if item in list(pairs.values())[i]:
        print(list(pairs.keys())[i])
        break
