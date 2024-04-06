'''
polymorphism:
poly=many
morph=form

1.Overloading
    a.Operator overloading
    +-->addition of 2 numerical data types
    +--->combining 2 strings
    --->Extending  list with a element of another list 
    b.Method overloading
    c.constructor overloading
        
2.Overriding:
a.Method over-riding
b.

'''
#Operator overloading
#from pip._vendor.typing_extensions import overload

'''
print(2+4.9)
print("2"+"4")
print([1,2,3,4]+[4,5,6,7])

'''
#Method Overloading

class Example:
    def __init__(self,*b):  #constructor overloading with the help of variable length arguments
        print(b)        
    
    def method_one(self,*a):     #method overloading with the help of variable length arguments
        print(a)

    def method_two(self,a=0,b=0,c=0,d=0):   #method overloading with default values
        print(a+b+c+d)
        
    
'''      
class Example:
    def method_one(self):
        print("This is the  method without parameter")
        
        @overload
        def method_one(self, a):
            print(f"This is the Method with one parameter {a}")
            
        @overload    
        def method_one(self, a,b):
            print(f"This is the Method with two parameter{a} and {b}")     
'''   
              
obj=Example(1,2)
obj.method_one(1,3,4)
obj.method_one(1,3,4,5,6)
obj.method_one(5,4)   
obj.method_two ()        