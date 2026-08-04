#the diff between tuple and list are that tuples are immutable (means they cannot be changes) where 
#as the lists are mutable(means the can be changed)
#tuples are recognized by () and lists are recognized by []
a=(1,2,3,4,5)
print(a)

#list
al = [100,200]
print(al)
al[0] = 0
print(al)
del al[0]
print(al)

# del a[0] #this will give an error because tuples are immutable
# print(a)
# a[0] = 20 #this will give an error because tuples are immutable
# print(a)
print(a.count(2))
print(a.index(3))
print(a.index(5))

#convert tuple to list
al = list(a)
#convert list to tuple
a = tuple(al)
