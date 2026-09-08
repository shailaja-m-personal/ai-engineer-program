import pandas as pd

l1 = ('converting', 'numpy', 'dictionary')
my_list = [1,2,3]
d = {'name' : 'R', 'age' : 2, 'class' : 30}

# print(pd.Series(data = l1))
# print(pd.Series(data = l1, index=[10,11,12]))
# print(pd.Series(data=my_list))
# print(pd.Series(data=d))

ser1 = pd.Series(data = [10,20,30,40,50,60,70], index=['a','b','c','d','e','f','g'])
# print(ser1.size) 
# print(ser1.ndim)
# print(ser1.shape) #row, col,
# print(ser1)
# print(ser1[['d']])
# print(ser1['b':'d'])
# print(ser1.index[0])
ser_str = pd.Series(data = [10,20,'50'], index=['a', 'b', 'c'])
print(ser_str.dtype)
print(ser_str.astype(float))  #type conversion from object to float
ser3 = pd.Series()



