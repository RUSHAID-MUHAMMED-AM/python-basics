# Create an abstract class called ElectronicDevice.

# Add these three abstract methods:

# turn_on()

# use()

# turn_off()

# Create two child classes:

# Smartphone

# Laptop

# Implement the methods with device-specific messages.

# Create objects and show how both devices behave.



from abc import ABC, abstractmethod
class ElectronicDevice(ABC):
     @abstractmethod
     def turn_on(self):
        pass
    
     @abstractmethod
     def use(self):
         pass
     
     @abstractmethod
     def turn_off(self):
         pass
     
class SmartPhone(ElectronicDevice):
    def turn_on(self):
        print("Smartphone is turning on...")
        
    def use(self):
        print("Opening apps and making calls...")
    
    def turn_off(self):
        print("Smartphone is shutting down.")
        
        
class LapTop(ElectronicDevice):
    def turn_on(self):
        print("LapTop is turning on...")
        
    def use(self):
        print("Running software and browsing internet...")
    
    def turn_off(self):
        print("Laptop is shutting down.")
obj_1=SmartPhone()
obj_2=LapTop()
obj_1.turn_on()
obj_1.use()
obj_1.turn_off()


obj_2.turn_on()
obj_2.use()
obj_2.turn_off()