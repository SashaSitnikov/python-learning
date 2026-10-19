def delete_contact_one(contacts, name):
    if name in contacts:
        del contacts[name]
        return True
    else:
        return False

def delete_contact_two(contacts, name):
    result = contacts.pop(name, None)
    return result is not None

def delete_contact_three(contacts, name):
    try:
        del contacts[name]
    except KeyError:
        return False
    return True

contacts = {"Alex": 22, "John": 72, "Mia": 11}
name = "Alex"

print(delete_contact_one(contacts, name))
print(delete_contact_two(contacts, name))
print(delete_contact_three(contacts, name))
