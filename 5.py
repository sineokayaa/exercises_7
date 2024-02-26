n = int(input())
dscndnts = {}
for i in range(n):
    name = input().split()
    value = []
    if name[0] in list(dscndnts.keys()):
        value = dscndnts[name[0]]
        value.append(name[1])
        dscndnts[name[0]] = value
    else:
        value.append(name[1])
        dscndnts[name[0]] = value

def dscndnt(name, count):
    if name not in dscndnts.keys():
        return count[0]
    count[0] += len(dscndnts[name])
    for i in range(len(dscndnts[name])):
        dscndnt(dscndnts[name][i], count)
    return count[0]


count = [0]
print(dscndnt(input(), count))
