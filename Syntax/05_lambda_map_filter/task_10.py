# 1
grades = {
    "Аня": [5, 4, 5],
    "Олег": [3, 4, 3],
    "Мила": [5, 5, 4],
    "Ян": [2, 3, 3],
    "Кира": [4, 4, 5],
}

averages = {name: sum(marks) / len(marks) for name, marks in grades.items()}
passed = [(name, avg) for name, avg in averages.items() if avg >= 4]
top3 = sorted(passed, key=lambda pair: pair[1], reverse=True)[:3]

for place, (name, avg) in enumerate(top3, start=1):
    print(f"{place}. {name}: {avg:.2f}")
