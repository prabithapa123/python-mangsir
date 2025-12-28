people = ['John', 'Paul', 'Sara', 'Susan']

for person in people:
    if person == 'Sara':
        continue
    print(f'Current person: {person}')


for i in range(len(people)):
    print(people[i])

i = 0
while i < 10:
    print(i)
    i = i + 1