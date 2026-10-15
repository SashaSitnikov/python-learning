with open("t1.txt", "r", encoding="utf-8") as r, open("t2.txt", "w", encoding="utf-8") as w:
    for line in r:
        w.write(line)

with open("a.png", "rb") as src, open("b.png", "wb") as dst:
    while chunk := src.read(1024):
        dst.write(chunk)