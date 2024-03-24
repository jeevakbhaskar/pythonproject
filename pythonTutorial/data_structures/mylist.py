'''
List:
1.An empty list
2.Heterogeneous(opp.homegeneous)
3.Accessing elements from the list
    a.by using Index
    b. by using Slice
    c: by using loops
    
4.list is mutable
5.list stores duplicate values
6. Insertion order is preserved-   

'''

'''
a=[] # 1.we can check empty list
print("a",type(a))
print(a)

b=[]
'''

c=list(range(2,21,2))
print("c-->",c)

d=[1,2,3,4]
print(d)

c.append(56) # append value
print("c after  appending 56-->")
print(c)

#c.append(d) # append value
#print("c after  appending d-->")
#print(c)

print(c[10])
#print(c[11])

c.extend(d)
print(("c after extending with d-->"))
print(c)

#c.clear()
#print(c)

e=c.copy()
print("e-->",e)

print(c.index(4,2))

c.insert(9, 100)
print(c)


print(c.pop(8)) # remove last element in the list with specified index
print(c)

c.remove(56)
print(c)

c.reverse()
print(c)

c.sort()
print(c)

print(c.count(100))

print(len(c))


f=[1,2,3,4 ]

print(f)
print 

