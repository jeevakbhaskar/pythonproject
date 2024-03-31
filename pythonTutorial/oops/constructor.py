'''
Constructor: is a method used to construct an object.
1. Constructor is not Mandatory.
2.Constructor will be called implicitly  when an object is created  (This is a constructor
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_init_', 'display_details']
)

3.Constructor can be defined with/without parameter  
'''
class Humanbeing():
    def _init_(self):   # constructor no  parameters 
        print("This is a constructor")
        
    def display_details(self):
        print("This is a Human being method")
         
shashi=Humanbeing()        
shashi.display_details()  #Explicitly method
shashi._init_()         #implicitly method

print(dir(shashi))