'''
Exception handling:Handling of abnormal/unexpected behaviors

Types of errors:

    1.Compile time Error: This is can't be handled. Developer/coder/programmer is solely responsible   for this.  
    2.run time Error:These are unexpected errors  and can be handled.


How to handle exception?

1>using single try-single except default block
2>using single try-specific except block
3>using single try -multiple specific except blocks
4>using single try -multiple specific except and single except default block
5>nested try-except  blocks
6>try -except-finally
7>try-except block

'''
print(1+2)  #3
print(6-3)  #3
print(4*6)  #24
try:  
    #101=11 # compile time error 
    try:
       # a=[2,3,4] 
        #print(a[4])
        
        print(9/0)  # which condition given corresponding except block can run give the output
    except ZeroDivisionError:
        print("9/0-->ZeroDivisionError: division by zero")   
    
except TypeError:
    print("Type Error:Unsupported operand type(s) for /:'int' and  'str' ")

except Exception as e: #default except block
        print("Exception thrown at line 31",e)
finally:
    print("This is 'finally' block")        
        
print(2**4) #16
print(9//4) #2