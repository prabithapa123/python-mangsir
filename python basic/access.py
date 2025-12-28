class Person:
    def __init__(self, name, age, password):
        self.name = name
        self._age = age
        self.__password = password

    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = password
    

person = Person("ram", 12, 123)
print(person.name)
print(person._age)
person.set_password("OKdkd")
print(person.get_password())
# print(person.__password)

