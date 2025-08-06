class Car:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

car_1=Car("BMW",2020)
car_2=Car("Toyota",2023)

print(car_1.brand,car_1.year)
print(car_2.brand,car_2.year)
