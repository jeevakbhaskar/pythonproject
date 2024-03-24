'''
swap the values using third variable
'''
x=30
y=50

temp=x
x=y
y=temp

print("X:",x)
print("Y:",y)

'''
swap the values without  third variable
'''
x=30
y=20

x,y =y,x

print("X:",x)
print("Y:",y)

''' 
score=int(input("please enter your score:"))

if score>=35:
    print("exam is passed")
else:
    print("exam is failed")    
    
  
    
age=int(input("please enter your age:"))

if age>=18:
    print("allowed to vote")
else:
    print("Not allowed to vote")    
 ''' 
    
year=int(input("please enter year checked:"))

if (year%4==0 and year%100!=0 or year%4==0):
    print("The year is a leap year")
else:
    print("The year is not  a leap year")    


