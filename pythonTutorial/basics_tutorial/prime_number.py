'''
Created on Mar 23, 2024

@author: Administrator
'''
a=int(input("please enter a number:"))

for i in range(2,a+1):
    b=a%i
    if b==0 and i<a:
        print("Not a prime number")
        break
    if  b==0 and i==a:
        print("prime number")