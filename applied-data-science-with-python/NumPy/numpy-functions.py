import numpy as np
# import numpy.random as random

# np.random.seed(10)
# h = np.random.randn(10)
# print(h)
# arr = np.random.randint(1,25)

# # random.seed(10)
# # h = random.randn(10)
# # print(h)

# nparray_1 = np.array((1,2,3))
# a = 2.211115887744
# np.round(np.sqrt(arr),1)

# calculate the standard deviation
arr = np.array([1, 2.2343, 3.454, 40.97])
print(arr)
print(np.std(arr)) #std = sqrt(var)
print(np.around(arr)) #round(value, decimal place value)
print(np.abs(-5)) #convert -ve to +ve
arr = np.array([1,2,3,4])
print(np.cumprod(arr))
print(np.cumsum(arr))
arr = np.array([10,2,3,4,-1])
print(np.argmax(arr)) #return indexes
print(np.argmin(arr))

# calculating the square
arr = np.array([1,2,3,4])
arr*2, arr*3 #square / cube of the values
pow(arr, 3)
np.power()