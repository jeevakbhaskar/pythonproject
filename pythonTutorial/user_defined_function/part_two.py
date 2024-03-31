'''
Types of arguments
1.formal arguments 
    a.default arguments
    b.variable length (positional )arguments
    c.variable length arguments
2.Actual arguments
    a.positioanal arguments 
    b.keyword arguments
    
    
special cases:
passing a keyword arguments and positional arguments are same function
'''
def add(a=0,b=0):#default  formal arguments
    print("a--->",a)
    print("b-->",b)
    c=a+b
    print("sum-->",c)

def addition(*a): #variable length arguments
    print(a) 
    c=0
    for i in a:
        c=c+i
        print(c)
        
def display_details(**a): #variable length arguments
     print(a)     
       
def mixed_v_arg(*a,**b):   
    print(a, b)            
        
add(4,2) #positional arguments
add(b=4,a=2) #keyword arguments
add(8,b=6) #
#add(a=8,6) #syntax error-possitional arguments can't passed after the keyword argument
add(2)
add(7,a=3)#syntax error-multiple values for argument a
addition(1,2,3,4,5)
display_details(a=1,b=2,c=4,d=5)

mixed_v_arg(1, 2, 3, 4, c=3, d=4, e=5)
# mixed_v_arg(c=3, d=4, e=5, 1, 2, 3, 4)


