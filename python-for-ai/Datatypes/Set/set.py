s = {1,2,3,4,5,6,7,8,9,10,1,2}
print(type(s)) #type(input)
print(s) #printing the set

#type casting to list
list_set = list(s)
print(type(list_set)) #type(input)  
print(list_set) #printing the list

#cannot access the elements of a set using index as it is unordered collection of data
#s.index(1) #this will give an error as set is unordered collection of data
#empty set
s1 = set()
print(type(s1)) #type(input)
print(s1) #printing the empty set
s1 = {"apple", "banana", "cherry", "kiwi", "mango",1,1,1,1,1}
print(s1) #printing the set

#set methods
#length of the set - len()
print(len(s1)) #printing the length of the set

#remove an element from the set - remove()
s1.remove("kiwi")
print(s1) #printing the set after removing an element

#trying to remove an element that is not present in the set will raise a KeyError
# s1.remove("orange") #this will give an error as "kiwi" is not present in the set
# print(s1) #printing the set after trying to remove an element that is not present in the set

#adding an element to the set - add()
s1.add("orange")
print(s1) #printing the set after adding an element
s1.add(67)
print(s1) #printing the set after adding an element
s1.add("watermelon")    
print(s1) #printing the set after adding an element

#update() method is used to add multiple elements to the set
s1.update(["grapes", "papaya", "pear"])
print(s1) #printing the set after adding multiple elements
s1.update([1, "berry"])
print(s1) #printing the set after adding multiple elements

#difference between two sets - difference()
s2 = {1, 2, 3, 4, 5, "grapes", "papaya", "pear"}
print(s1.difference(s2)) #printing the difference between two sets
print(s2.difference(s1)) #printing the difference between two sets

#difference_update() method is used to remove the elements of another set from the set
s1.difference_update(s2)
#print(s1) #printing the set after removing the elements of another set
s2.difference_update(s1)
print(s2) #printing the set after removing the elements of another set

#intersection() method is used to return the common elements of two sets
s3 = {1, 2, 3, 4, 5, 'grapes', 'papaya', 'watermelon', 'banana'}
print(s1)
print(s3)
print(s1.intersection(s3)) #printing the common elements of two sets

#intersection_update() method is used to update the set with the common elements of two sets
s1.intersection_update(s3)
print(s1) #printing the set after updating with the common elements of two sets
s3.intersection_update(s1)
print(s3) #printing the set after updating with the common elements of two sets

#union() method is used to return the union of two sets
set1 = {1, 2, 3, 4, 5}    
set2 = {5,6}
print(set1.union(set2)) #printing the union of two sets
print(set2.union(set1)) #printing the union of two sets
set2 = set1.union((90,91))
print(set2) #printing the set after adding multiple elements
set2.update([92,93])
print(set2) #printing the set after adding multiple elements