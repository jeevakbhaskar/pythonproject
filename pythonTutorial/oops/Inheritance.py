'''
Inheritance:
1.Single level Inheritance(GrandFather---->Father)
2.Multi level Inheritance(GrandFather---->Father------>child)
3.Multiple Inheritance(Father,Mother---->child)

Method Resolution Order(MRO) [<class '__main__.child'>, <class '__main__.Father'>, <class '__main__.GrandFather'>, <class '__main__.Mother'>, <class 'object'>]

'''
class GrandFather:
    def gf_method(self):
        print("This is Grandfather method")
        
class Father(GrandFather):
    def f_method(self):
        print("This is father method")
        
    def car(self):
        print("This is Father's car")
        
class Mother():
    def m_method(self):
        print("This is mother's method")
        
    def car(self):
        print("This is Father car")
        
        
class child(Father,Mother):   #which order method is called then print the message
    def c_method(self):
        print("This is child method")   
        
    def car(self):
        print("This is My car")
        Father.car(self)
        Mother.car(self)
        

print("=============GrandFather Class=======")  
      
ajja=GrandFather()
appa=Father()
ajja.gf_method()

print("======Father Class=========")

ajja.gf_method()
appa.f_method()
#appa.gf_method()

print("====Child Class====")

myself=child()
myself.c_method()
myself.gf_method()
myself.f_method()
myself.m_method()
myself.car()

print("===========MRO===============")
print(child.mro())
