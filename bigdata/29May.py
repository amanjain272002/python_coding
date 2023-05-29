import numpy as np

# ar1 = np.array([[1,2,3],[4,5,6]])
# ar2 = np.array([[7,8,9],[10,11,12]])
# print((ar1+ar2).shape)
# print(ar1-ar2)
# print(ar1*ar2)
# print(ar1/ar2)

# ar3 = np.array([10,20,30])
#  first rank array
# print(ar3.shape)
# print(ar3.ndim)

# ar1 = np.array([[1,2,3],[4,5,6]])
# print(ar1+3)


# ar1 = np.array([[1,2,3],[4,5,6]])
# ar3 = np.array([10,20,30,90])
# print(ar1+ar3)



# ar3 = np.array([10,20,30])[np.newaxis]
# print(ar3)
# print(ar3.shape)
# print(ar3.ndim)
# ar3 = ar3.T
# print(ar3)
# print(ar3.shape)
# print(ar3.ndim)

# or

ar4 = np.array([12,13,14])
print(ar4.ndim)
print(ar4.shape)
ar4 = ar4.reshape(1,3)
print(ar4)
print(ar4.ndim)
print(ar4.shape)