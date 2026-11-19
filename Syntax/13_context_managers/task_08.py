from pathlib import Path
from contextlib import contextmanager


@contextmanager
def safe_write(path):
    path = Path(path)
    tmp = path.with_name(path.name + ".tmp")
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            yield f
        tmp.replace(path)
    finally:
        tmp.unlink(missing_ok=True)

with safe_write("test.txt") as f:
    f.write("Новый текст")

print(Path("test.txt").read_text(encoding="utf-8"))

try:
    with safe_write("test.txt") as f:
        f.write("Этот текст не должен сохраниться")
        raise ValueError("Ошибка записи")
except ValueError as e:
    print(f"Ошибка: {e}")

print(Path("test.txt").read_text(encoding="utf-8"))
