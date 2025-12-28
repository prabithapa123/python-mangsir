class House:    
    def __init__(self, name, window=5, color="purple", door=3):
        self.window = window
        self.color = color
        self.door = door
        self.name = name
    
    # def __str__(self):
    #     return self.name
    
    def set_color(self, color):
        self.color = color
        
    def get_color(self):
        return self.color 
    
    def __gt__(self, value):
        return self.window == value.window
        
prabee = House(name="prabee")
print(prabee)
# jon = House(window=2, color="green", door=5)
# print(jon.get_color())
print(prabee.__gt__(123))