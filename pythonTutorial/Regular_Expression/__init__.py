'''
Regular expression (REgEx):REgEx is used  for validating input
'''
import re

#a="SS89shashikala"

a="SS 78966 shashi"
b="sahshikalasmys.@gmail.com"

print(re.search("shashikala",a))        #<re.Match object; span=(0, 10), match='shashikala'>
print(re.search("s.",a))                #<re.Match object; span=(0, 2), match='sh'>
print(re.search("^s",a))                #<re.Match object; span=(0, 1), match='s'>
print(re.search("sha",a))            #<re.Match object; span=(0, 6), match='shashi'>
print(re.search("s+",a) )                #<re.Match object; span=(0, 1), match='s'>
print(re.search("s*",a))                #<re.Match object; span=(0, 4), match='ssss'>
print(re.search("s?",a))                #<re.Match object; span=(0, 1), match='s'>
print(re.search("\\s",a))               #<re.Match object; span=(2, 3), match=' '>
print(re.search("\d{1,2}",a))            #<re.Match object; span=(2, 4), match='89'>
print(re.search("\w{0,6}",a))               #<re.Match object; span=(0, 6), match='SS89sh'>
print(re.search("//",a))                    #None

print(re.sub("\d","*",a,6))         #sssss*****shashi
print(re.subn("\d","*",a,6))        #('sssss*****shashi', 5)

print(re.split("\s",a,3))           #['SS', '78966', 'shashi']

print(re.findall ("/s",b))