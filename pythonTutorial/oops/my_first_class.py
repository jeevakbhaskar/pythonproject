'''
Method=every function defined 

class is a blue print
1.Inheritance
2.Polymorphism
3.Data Abstraction
4.Encapsulation

 
'''


#defining a class
class Humanbeing():
        def __init__(self,name,color,height,gender):
            self.name=name
            self.color=color
            self.height=height
            self.gender=gender
            
        def display_details(self):
            print(f"I am  a Human being in{self.name}:name,{self.color}:color,{self.height}:feet,{self.gender}:gender")
            
vivek=Humanbeing("shashi","black",5.6,"male")  # Instantiation an  created  object vivek 
vivek.display_details() # call the method  

#shashi=Humanbeing()
#shashi.display_details("white",5.8,"male")

print(type(vivek))
print(id(vivek))
#print(self.name(vivek))

#print(type(shashi))
#print(id(shashi))