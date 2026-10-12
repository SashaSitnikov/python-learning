users = [{"name": "Аня", "age": 25}, {"name": "Олег", "age": 19},
         {"name": "Мила", "age": 31}, {"name": "Ян", "age": 22}]

users = sorted(users, key=lambda u: u["age"], reverse=True)
names = list(map(lambda u: u["name"], filter(lambda u: u["age"] > 21, users)))
print(names)
