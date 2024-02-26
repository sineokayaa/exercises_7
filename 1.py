str = input()
str_lst = str.split()
str_dict = {}

for i in range(len(str_lst)):
    str_dict[str_lst[i]] = str_lst.count(str_lst[i])

while str_dict != {}:
    i = max(list(str_dict.values()))
    num = list(str_dict.values()).index(i)
    print(list(str_dict.keys())[num])
    str_dict.pop(list(str_dict.keys())[num])
