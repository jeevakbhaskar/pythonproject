'''
1.To validate Mobile number
-have 10 digits
- 1St digit should be any digit from 5-9
-remaining digits can any digit from 0-9

RE-[5-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]
    -"[5-9][0-9]{9}" 
    -"[5-9]\d{9}" 
'''
import re
from re import fullmatch
number=input("Please enter a Phone number:")
#my_re="[5-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"      
my_re="[5-9][0-9]{9}"  
match_object=re. fullmatch(my_re,number)            #Please enter a Phone number:8904124740
                                                   # <re.Match object; span=(0, 10), match='8904124740'>
                                                    #You Entered  a valid phone number

print(match_object)

if match_object !=None:
    print("You Entered  a valid phone number")
else:
    print("You Entered an invalid phone number")