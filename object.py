class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display_info(self):
        print(f"students Name = {self.name}")
        print(f"students age = {self.age}")
        print(f"students grade = {self.grade}")
    
student_1=Student("Anu",21,"A") 
student_2=Student("Ravi",20,"B") 
student_1.display_info()
student_2.display_info()