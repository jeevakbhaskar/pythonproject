'''
Data Abstraction : Existing an idea not implement
Types of method
1.Implement Method
2.UnImplement method

abstract class: a class having one or more abstract methods
- an abstract class can have both implemented and unimplented methods
-if an abstract class contains abstract methods

- Concrete classes, abstract class ,interfaces

Implementation Of abstraction: a class having one or more abstract method
1..from abc module import everything
2.Inherit ABC class into your abstraction
3.add @abstractrmethod decorator 

Note:we can't create an object from abstract class unless object is implemented
    we can't create an object  from  sub-classes(child class) Object is implemented
    
'''
from abc import 

class Car(abc):
    def __init__(self,color,seats,wheels=4):
        self.color=color
        self.seats=seats
        self.wheels=wheels
        print("Car Object is created Successfully")
          
def move_forward (slef):
    print("car is moving forward")
def move_backward(self):
    print("car is moving backword")
    
    @abstractmethod
def engine_specification(self):     #Un implement method
    print("Engine Specification")
    pass

class HatchBack(Car):
    def hb_function(self):
        print("This is Hatchback  class function ")
        
Car1=Car("red",8)
swift=HatchBack("white",4)        