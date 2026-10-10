letters = ["b", "a", "b", "c", "a"]
print(list(dict.fromkeys(letters)))


result = []
seen = set()

for letter in letters:
    if letter not in seen:
        seen.add(letter)
        result.append(letter)
        
print(result)