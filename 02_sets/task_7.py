lst = [3, 2, 1, 4, 5, 6, 7, 8, 9, 1, 5, 2, 8]

print(False if len(lst) == len(set(lst)) else True) 



seen = set()
for el in lst:
    if el not in seen:
        seen.add(el)
    else:
        print(True)
        break
else:
    print(False)







