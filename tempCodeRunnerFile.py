class House:    
    def __init__(self, window, color, door):
        self.window = window
        self.color = color
        self.door = door
    
    def set_color(self, color):
        self.color = color
        
    def get_color(self):
        return self.color 
        
prabee = House()
jon = House(window=2, color="green", door=5)
print(jon.get_color())