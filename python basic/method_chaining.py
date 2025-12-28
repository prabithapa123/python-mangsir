# class GrandFather:
#     def __init__(self):
#         print("Grandfather")

#     def get_house(self):
#         return self.house
#     house = "Luxury"

# class Father(GrandFather):
#     def get_house(self):
#         print(super().get_house())
#         return "New house"
    
# f1 = Father()
# print(f1.get_house())

from abc import ABC, abstractmethod


class Computer(ABC):
    def run(self, app):
        self.process(app)

    @abstractmethod
    def process(self, app):
        pass

class Mobile(Computer):
    def process(self, app):
        print("Mobile is running", app)

samsung = Mobile()
samsung.run("PUBG")

