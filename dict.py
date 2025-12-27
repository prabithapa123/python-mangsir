# person = {
#     'name': 'Prabee',
#     'age': 25,
#     'address': 'Kathmandu'
# }


# print(person, type(person))
# print(person['name'])
# print(person['age'])
# print(person.get('address'))

# person['phone number'] = '98520'
# print(person)

# print(person.keys())
# print(person.values())
# print(person.items())

# person2 = person.copy()
# person2['city'] = 'boston'
# print(person2)
# print(person)


# del person['age']
# print(person)
# person.clear()
# print(person)

people = [
    {'name':'Prabi', 'age':25},
    {'age':32},
    {'name':'Dom', 'age':27},
]

print(people[1]['age'])
print(people[1].get('name'))

