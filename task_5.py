numbers = [3, 1, 3, 2, 1, 3]
count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

max_count = max(count, key=count.get)
print(max_count)



