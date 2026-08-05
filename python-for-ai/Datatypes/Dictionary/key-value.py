d = { 'name' :  'sam'   ,  
     'age'  :   23     ,
     'hair' :  'black',
     'language' : ['python','sql','R','java','c++'],
     'year' : 2026  }
print(d)

#printing only keys
print(d.keys())

#printing only values
print(d.values())

#printing both keys and values as a list of tuples
print(list(d.items()))

#printing last key-value pair and removing it from the dictionary
print(d.popitem())
print(d)

print(d.pop('age'))  #removing a key-value pair using pop() method  
print(d)

print(d.pop('color', 'color not present'))  #getting value of a key using get() method
print(d)