friends = {
    "Аня": {"Олег", "Мила"},
    "Олег": {"Аня", "Ян", "Мила"},
    "Мила": {"Аня", "Олег", "Кира"},
    "Ян": {"Олег"},
    "Кира": {"Мила"},
}

name1 = input()
name2 = input()
friend1 = ''
friend2 = ''

print(f'Общие друзья {name1} и {name2}: {friends[name1] & friends[name2]}\n')

recs1 = set()
for friend in friends[name1]:
    recs1 |= friends[friend] 
recs1 -= friends[name1] 
recs1.discard(name1)     
            


recs2 = set()
for friend in friends[name2]:
    recs2 |= friends[friend]    
recs2 -= friends[name2]         
recs2.discard(name2)             



print(f'Рекомендация от {name1}: {recs1}')
print(f'Рекомендация от {name2}: {recs2}')