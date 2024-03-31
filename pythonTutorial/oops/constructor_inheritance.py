'''

'''
class GrandFather:
    def __init__(self,name,age):
        self.name=name
        self.age=age      
         
        print("This is Gf Constructor")
        
    def gf_method(self):
        print(f"GF name is:{self.name} and {self.age} years old")  
        
class Father(GrandFather):
    
    def __init__(self,name,age,aadhar_id):       
        print("This is father class  Constructor")
        #self.name=name
        #self.age=age
        self.aadhar_id=aadhar_id
        
        #GrandFather.__init__(self,name,age)
        super().__init__(name,age)   
    
    def f_method(self):
        print(f"father name is :{self.name},{self.age} and {self.aadhar_id} ")
        
    def car(self):
        print("This is Father's car")   
        
print("======= GF===== ")
ajja=GrandFather("ajja",91)
ajja.gf_method()

print("======Father=======")
appa=Father("appa",91,10002)   
appa.f_method() 