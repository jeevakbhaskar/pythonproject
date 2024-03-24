'''
Operators: symbols which performs operations on one or more operands(variables)
1.Arithmetic operators:+,-,*,/,%,**,//  
2.logical operators:AND, OR, NOT 
3.Assignment operators: =
4.relational comparison  operators: >,<,>=,<=,==,!=    two operands
5.a.increment operators: +=
5.b. decrement operator:  -=
6.Membership operators: in, not in 
Identity operators:is



'''

'''
print("Arithmetic operators")
a=5
b=6
c=a+b

print(c)

a=int(input("please enter a:=")) #type casting
b=int(input("please enter b:="))
c=a//b
print("output:",c)

print(type(c))

print(2**3)
'''

'''
print("logical operators")
print(True and True)
print(True and False)
print(False and True)


print(True or True)
print(False or False)
print(False or True)

print(not True)
'''

'''
print("comparison operators")
print(5>8)  # False
print(5>=8) #  False   
print(5<=8) #  True
print(5<8) #  True
print(5!=8)  # True


print("increment operators:")
a=3
a=a+1
a+=1
print(a)

print("decrement operators")
a-=1
print(a)


'''
print("Membership operators:")
print('a' in 'shashikala')
print('A' not in 'shashikala')
print('bh'  in 'shashikala')


print("Identity operators:")
a=2
b=2
print(a is b)
print(id(a))
print(id(b))
