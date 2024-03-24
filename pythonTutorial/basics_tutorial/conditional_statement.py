'''
conditional statements:
1.if statement
2.if -else statement
3.Series if-else statement
4.Nested if-else statements  
logical operators  if statements
'''
age=int(input("please enter your age:"))

'''
if age>=13:
    print("allowed")
else:
    print("push them out")    
print('not allowed')
'''
'''

if age >18:
    print("you are an adult")
elif age>=13:
    print("you are a teenager")
else:
    print("you are a child")
    
print("program stopped")
'''



if age >13:
    if age>18:
        if age>60:
            print("you are an senior")
        else:
            print("you are an adult")
    else:
        print("you are a teenager")
else:
    print("you are a child")
    
print("program stopped")



if age>=13 and age<=18:
    print("you are an teenager")
else:
    print("program stopped")
