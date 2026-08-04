#reverses the list
list1 = ['1','100','3', 'A', [10,20,30]]
print(list1[::-1])
list1.reverse()
print(list1)
#reversed is a python inbuilt function which returns an iterator that accesses the given sequence in the reverse order.
#its not specific to list, it can be used with any sequence type.
print(list(reversed(list1)))