from pathlib import Path

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.readlines()
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
    else:
        print("Прочитано!")
    finally:
        print("Готово!")


BASE_DIR = Path(__file__).parent
path = BASE_DIR / "data.txt"

read_file(path)