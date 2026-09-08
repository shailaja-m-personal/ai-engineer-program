import numpy as np

print(np.arange(0.5, 5.5, 0.6))

l1 = np.array(range(1,101))
print(l1.ndim)
print(l1)

print(l1.size)

#reshape converts the 1 dimention array into n dimensional array
l3 = l1.reshape(10,10)
print(l3.ndim)
print(l3)

l1 = np.arange(1,16)
print(l1.ndim)
print(l1)

l3 = l1.reshape(3,5)
print(l3)
print(l3.ndim)

#Flattern converts n dimensional array into 1 dimensional array
print(l3.ndim)
l4 = l3.flatten()
print(l4)
print(l4.ndim)

np.random.seed(10)
h = np.random.randn(10)
print(h)