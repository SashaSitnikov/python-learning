levels = {}

def read_lines(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                yield line

def parse(lines):
    for line in lines:
        date, time_, level, message = line.split(" ", 3)
        yield {"date": date, "time": time_, "level": level, "message": message}
    

def only(records, level):
    for rec in records:
        if rec["level"] == level:
             yield rec

for rec in parse(read_lines("app.log")):
    if rec["level"] in levels:
        levels[rec["level"]] += 1
    else:
        levels[rec["level"]] = 1
        
print(f"Количество INFO: {levels['INFO']}\nКоличество WARNING: {levels['WARNING']}\nКоличество ERROR: {levels['ERROR']}")