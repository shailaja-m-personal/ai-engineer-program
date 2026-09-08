import numpy as np

ls = [20, 30, 40]
# print(type(ls))
# print(ls)
ls_nparray = np.array(ls)
# print(type(ls_nparray))
# print(ls_nparray)

nparray_1 = np.array((1,2,3))
# print(type(nparray_1))
# print(nparray_1)

#2D array
arr_2d = np.array([[10, 20, 45],
                   [78.1234, 56.563, 232.8976],
                   [10, 20, 30],
                   [5, 78, 45]])
# print("Dimension - ", arr_2d.ndim,  "\n", "Printing array - ", arr_2d,  "\n", "Shape -", arr_2d.shape, "\n", "Type - ", "\n", arr_2d.dtype, "\n", "another type - ", type(arr_2d))

#operations with multiple arrays
#adding 2 arrays of same shape
arr_3 = np.array([
                 [10, 20, 30],
                 [100, 200, 300],
                 [1, 2, 3],
                 [5, 6, 7]])
# print(arr_2d+arr_3)

#where function
arr_new = np.where(arr_3>=100, 0, arr_3)
# print(arr_3)
# print(arr_new)

arr_new = np.where(arr_3>=100, 0, -1)
# print(arr_3)
# print(arr_new)

arr_new = np.where(((arr_3>=100)|(arr_3==20)), 0, -1)
# print(arr_3)
# print(arr_new)

print(arr_2d)
# print(np.sum(arr_2d))
# print(np.max(arr_2d))
# print(np.min(arr_2d))
# print(np.mean(arr_2d))
# print(np.std(arr_2d))

# print(np.sum(arr_2d, axis=0))
# print(np.sum(arr_2d, axis=1))
# print(arr_2d[0]) #row1
# print(arr_2d[1]) #row2
# print(arr_2d[2]) #row3
# print(arr_2d[3]) #row4
# print(arr_2d[4]) #row5 -- no rows, throws error

# print(arr_2d[2:3])
#print(arr_2d[[3,0],:])
#print(arr_2d[[3,0],[2,1]]) 
#print(arr_2d[2:4, 1:3])
#print(arr_2d[:,2])
print(np.__version__)
