words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}

for word in words:
    key = tuple(sorted(word))
    groups[key] = groups.get(key, []) + [word]
print(list(groups.values()))



