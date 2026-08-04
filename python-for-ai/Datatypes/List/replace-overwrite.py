#using replace method you can change the element at a particular index
text_data = "using replace method you can change the element at a particular index"
text_data = text_data.replace("replace","overwrite")
print(text_data)

text_data = text_data.replace("ind","IND")
print(text_data)

list1 = ['1','100','3', 99]
list1[0] = 100
print(list1)
list1[3] = 'new'
print(list1)
print(list1[0:3])
print(list1[3])
