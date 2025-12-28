# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
        
#     def get_grade(self):
#         return self.grade


# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
        
#     def add_students(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
    
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
            
#         return value / len(self.students)
        
        
# s1 = Student('Tim', 25, 90)
# s2 = Student('Tim', 25, 80)
# print(s1.get_grade())
# c1 = Course('Science', 2)
# c1.add_students(s1)
# c1.add_students(s2)
# print(c1.get_average_grade())

# Inheritance
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def show(self):
#         print(f'Hey my name is {self.name} and I am {self.age} years old')

# class Dog(Pet):
#     def speak(self):
#         print("Bark")
                
# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age) # Calls the __init__ of parent class
#         self.color = color
        
#     def speak(self):
#         print("Meeow")

#     def show(self):
#          print(f'Hey my name is {self.name} and I am {self.age} years old and I am {self.color}')

# p = Pet('bill', 12)
# p.show()

# d = Dog("Tom", 10)
# d.show()

# c = Cat('Tommy', 15, 'orange')
# c.show()
    
# Class Attributes

# class Person:
#     number_of_people = 3
    
#     def __init__(self, name):
#         self.name = name
#         Person.add_person()

#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people

#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1
        
# p = Person("Hello")
# print(Person.number_of_people)

class Math:
    @staticmethod
    def add(x):
        return x + 5
    
print(Math.add(10))
