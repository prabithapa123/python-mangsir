fruits = ['Apple', 'Oranges', 'Grapes', 'Pears']
numbers = [1,2,3,4,5,6]
print(numbers[2])
print(fruits[2])


print(len(fruits))
fruits.append('Papaya')
print(fruits)

fruits.remove('Apple')
print(fruits)

fruits.insert(2, 'Apple')


fruits.pop(2)
print(fruits)
print(fruits)

items = ['mobile', 'computer', 'speaker']
items.insert(1, 'printers')
items.remove('computer')
items.append('batteries')
items.sort(reverse=True)
print(items)
