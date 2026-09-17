import pandas as pd

x = pd.DataFrame({'name': ['AB', 'Gayle', 'virat', 'wade' , 'warner'],
                  'age': [34,23,56,22 , 33],
                  'contact': [22,66,56,78, 32]})
   
y = pd.DataFrame({'name': ['AB', 'Gayle', 'virat', 'wade' , 'Rohit'],
                  'country': ['SA', 'WI', 'India', 'AUS','India'],
                  'Jersey': [17,333,18,15,45]})

# inner_merge_op = pd.merge(left = x, right = y, on = 'name', how = 'inner') #inner merge will give the common values of the two dataframes
# print(inner_merge_op)

# outer_merge_op = pd.merge(left =x, right = y, on = 'name', how = 'outer') #outer merge will give all the values of the two dataframes
# print(outer_merge_op)

# left_merge_op = pd.merge(left = x, right = y, on = 'name', how = 'left') #left merge will give all the values of the left dataframe and common values of the right dataframe
# print(left_merge_op)

# right_merge_op = pd.merge(left = x, right = y, on = 'name', how = 'right') #right merge will give all the values of the right dataframe and common values of the left dataframe
# print(right_merge_op)

another_merge_op = pd.merge(left = y, right = x, on = 'name', how = 'left') #left merge will give all the values of the left dataframe and common values of the right dataframe
print(another_merge_op)