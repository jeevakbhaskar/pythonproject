'''
Types of variables:
1.Instance/Object variables
2.Static/class variables
3.Local variables

Note:1.Instance variable can be declared anywhere with the help of self keyword. 
    2. Instance variable can be declared anywhere with the help of  class name 
'''
class Student():
    school_name="iquest"  # static/class  variable
    
    def _init_(self,name,roll_no):
        self.name=name  # Instance variables
        self.roll_no=roll_no
        
    def display_details(self):
        print(f"{self.name} has {self.roll_no} roll no" The is from {Student.school_name} )
        
    def display_total_score(self,english,science,maths):
        self.enlish=english
        total=english+science+maths
        print(f"{self.name} has scored{total}")
        
    def display_english_score(self):
        print(self.english)