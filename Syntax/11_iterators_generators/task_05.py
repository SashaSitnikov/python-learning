from pathlib import Path

FILE_PATH = Path(__file__).parent / "test_lines.txt"

def read_lines(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                yield line
                
def bad_read_lines(path):
    with open(path, encoding='utf-8') as f:
        return (line.strip() for line in f if line.strip())

print("Тест правильной версии")
for line in read_lines(FILE_PATH):
    print(f"Поймали строку: '{line}'")


print("\nТест неверной версии")
try:
    gen = bad_read_lines(FILE_PATH)
    print(next(gen))
except ValueError as e:
    print(f"Поймали ошибку: {type(e).__name__}: {e}")