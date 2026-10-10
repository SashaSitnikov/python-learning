names = ["  Аня ", "олег", " МИЛА  ", "", "ян"]
filter_names = [i.strip().capitalize() for i in names if i != ""] # strip убирает пробелы с обоих краев, capitalize делает первую букву заглавной
print(filter_names)