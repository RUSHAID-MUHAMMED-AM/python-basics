class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display_info(self):
        print(f"Name is {self.name}, {self.age} years old")
        
class Teacher(Person):
    def __init__(self,name,age,subject):
        self.subject=subject
        super().__init__(name,age)
    def display_info(self):
        super().display_info()
        print(f"Subject is {self.subject}")
        
p1=Teacher("Rushaid",24,"python")
p1.display_info()