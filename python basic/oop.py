# def person(name, age):
#     print(f'my name is {name} and i am {age} years old')


# person("Prabee", 25)


# def sum(*nums):
#     sum = 0
#     for i in nums:
#         sum = sum + i
#     print(sum)

# sum(1,2,3,4,5)

# #task
# def person(*names):
#     for i in names:
#         print(f'my name is {i}')

# person("ram", "laxman", "hanuman")

# def person(**details):
#     print(details['name'])
#     print(details['age'])
#     print(details['address'])

# person(name="Prabee", age=25, address = "Ktm")

# def star(func):
#     def wrapper():
#         print("*"*10)
#         func()
#         print("*"*10)
#     return wrapper

# # @star
# def hello():
#     print("Hello")

# star(hello)()

# fruits = ['apple', 'banana', 'papaya', 'cherry']
# print(fruits.index('banana'))
# fruits.sort()
# fruits.reverse()
# print(fruits)

# mydict = {
#     'name':'myname',
#     'age':12
# }

# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())

# print(mydict.get('name'))

class Person():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def set_age(self, age):
        self.age = age
    
    def get_age(self):
        return self.age
    
prabee = Person(name="Prabee", age=12, address="Ktm")
print(prabee.get_age())
prabee.set_age(25)
print(prabee.get_age())

print("Changes done from github")
