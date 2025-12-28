class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greet(self):
        return f'Hello, {self.name}'

    def has_birthday(self):
        return int(self.age) +1


p = User('Prabi', 'p@gmail.com', '27')
print(p.name)
print(p.email)
print(p.age)

print(p.has_birthday())
print(p.greet())


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greet(self):
        return f'Hello {self.name}, Your balance is {self.balance}'

janet = Customer('Janet', 'janet@gmail.com', '25')
janet.set_balance(500)
print(janet.greet())