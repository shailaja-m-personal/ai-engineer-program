#pop (index), The POP method removes the element using its index number.
#if no index is provided, it removes element at last -1 index
list1 = ['1','100','3','A']
print(list1)
list1.pop() #default index is -1
print(list1)
list1.pop(1) #removes element at index 0
print(list1)
del list1[0] #removes element at index 0
print(list1)
