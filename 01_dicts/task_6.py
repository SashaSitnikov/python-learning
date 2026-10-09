keys = ["a", "b", "c"]
values = [1, 2, 3]
result1 = {}

for i in range(3):
    result1[keys[i]] = values[i]

result2 = dict(zip(keys, values))