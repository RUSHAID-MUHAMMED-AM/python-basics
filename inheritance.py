class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
       
    
    def show_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department
      
    
    def show_details(self):
        super().show_details()
        print(f"Department: {self.department}")

# Create object and test
m1 = Manager("Ayesha", "M102", "Sales")
m1.show_details()