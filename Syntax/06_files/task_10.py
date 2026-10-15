from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.txt"


def load_tasks(path):
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def save_tasks(path, tasks):
    with open(path, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


def main():
    tasks = load_tasks(TASKS_FILE)
    while True:
        print("1. Добавить  2. Показать  3. Удалить  4. Выход")
        choice = input("Выбор: ")
        if choice == "1":
            tasks.append(input("Задача: "))
            save_tasks(TASKS_FILE, tasks)
        elif choice == "2":
            load_tasks(TASKS_FILE)
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
        elif choice == "3":
            del_task = int(input("Введите номер задачи: "))
            if del_task > 0 and del_task <= len(tasks):
                tasks.pop(del_task - 1)
                with open(TASKS_FILE, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                            
                del lines[del_task - 1]
                            
                with open(TASKS_FILE, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                print("Успешно!")
            else:
                print("Ошибка! Выберите корректный номер задачи")
        elif choice == "4":
            break
        else:
            print("Ошибка! Выберите другой вариант")


main()

