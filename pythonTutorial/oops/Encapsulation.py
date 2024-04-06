'''
Encapsulation:Wrapping up of data into single entity

Capsule:A small changes 

1.Protected data elements:

2.Private data elements:


'''
class Parent:
    def __init__(self,name):
        self._name=name
        
        def display_details(self):
            print(f"parent name is{self._name}")
            
p1=Parent("amma")
#p1.display_details()
#print(p1._name)

class Parent:
    def __init__(self,name):
        self.__name=name
        
        def display_details(self):
            print(f"parent name is{self.__name}")
            
p1=Parent("amma")
#p1.display_details()
#print(p1._parent_name)  name mangling technique
print(dir(p1))