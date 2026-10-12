students = [("Аня", 5), ("Олег", 4), ("Мила", 5), ("Ян", 3), ("Кира", 4)]

ranked = sorted(students, key=lambda s: (-s[1], s[0]))
print([name for name, grade in ranked])
