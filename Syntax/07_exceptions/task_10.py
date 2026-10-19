from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.txt"


def load_tasks(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []
    except UnicodeDecodeError:
        print("Не получается прочитать файл!")
        return []


def save_tasks(path, tasks):
    try:
        with open(path, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")
    except OSError as e:
        print(f"Ошибка при сохранении файла: {e}")
        return False
    else:
        return True
            
def read_int(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Вы не ввели целое число, попробуйте еще раз!")
        else:
            return number


def main():
    tasks = load_tasks(TASKS_FILE)
    while True:
        print("1. Добавить  2. Показать  3. Удалить  4. Выход")
        choice = read_int("Выбор: ")
        if choice == 1:
            tasks.append(input("Задача: "))
            save_tasks(TASKS_FILE, tasks)
        elif choice == 2:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif choice == 3:
            del_task = read_int("Введите номер задачи: ")
            if del_task <= 0:
                print("Ошибка! Выберите корректный номер задачи")
            else:
                try:
                    tasks.pop(del_task - 1)
                    print(save_tasks(TASKS_FILE, tasks))
                except IndexError:
                    print("Ошибка! Задачи с таким номером не существует")
        elif choice == 4:
            break
        else:
            print("Ошибка! Выберите другой вариант")


try:
    main()
except KeyboardInterrupt:
    print("\nВыход")

