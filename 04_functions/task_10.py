def common_friends(friends, a, b):
    return friends[a] & friends[b]


def recommendations(friends, name):
    recs = set()
    for friend in friends[name]:
        recs |= friends[friend] 
    recs -= friends[name] 
    recs.discard(name)
    return recs     


friends = {
    "Аня": {"Олег", "Мила"},
    "Олег": {"Аня", "Ян", "Мила"},
    "Мила": {"Аня", "Олег", "Кира"},
    "Ян": {"Олег"},
    "Кира": {"Мила"},
}

name1 = input()
name2 = input()


print(f'Общие друзья {name1} и {name2}: {common_friends(friends, name1, name2)}\n')
           

print(f'Рекомендация от {name1}: {recommendations(friends, name1)}')
print(f'Рекомендация от {name2}: {recommendations(friends, name2)}')