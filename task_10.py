students = {
    "Аня": {"math": 5, "physics": 4},
    "Олег": {"math": 3, "physics": 5},
}

average_grades = {}
for student, grades in students.items():
    average = sum(grades.values()) / len(grades)
    average_grades[student] = average
    print(f"{student}: {average:.2f}")
    
print(max(average_grades, key=average_grades.get))


