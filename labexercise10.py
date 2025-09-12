# Question 1

import numpy as np

arr = np.array([[100,200], [300, 400], [500, 600],[700,800]], dtype= np.uint16 )

print(arr)
print("array shape is:", arr.shape)
print("array dimensions are:", arr.ndim)
print("Length of each element of array in byte:", arr.itemsize)


#Question 2

import numpy as np

arr = np.arange(100,200,10).reshape(5,2)
print(arr)


#Question 3

import numpy as np

sampleArray = np.array([[11, 22, 33], [44, 55, 66],[77, 88, 99]]).reshape(3,3)
arr = sampleArray[:,2]
print("Printing Input Array")
print(sampleArray)
print("Printing array of items in the third column from all rows")
print(arr)


#Question 4

import numpy as np

sampleArray =np.array([[3,6, 9, 12],[15,18, 21, 24],[27,30, 33, 36], [39,42, 45, 48], [51,54, 57, 60]]).reshape(5,4)
arr = sampleArray[1::2, 0::2]
print(sampleArray)
print("###############################")
print(arr)


#Question 5

import numpy as np

arr1 = np.array([[5, 6, 9], [21,18, 27]])
arr2 = np.array([[15,33, 24], [4,7, 1]])

arr3 = arr1 + arr2
print(arr3)

arr4 = arr3 * arr3
print(arr4)


# Question 6

import numpy as np

arr = np.arange(10,34,1).reshape(8,3)

arr1 = np.split(arr,4,axis=0)

print(arr)
print("######################")
print(arr1)


#Question 7

#CASE 1
import numpy as np
sampleArray = np.array([[34,43,73], [82,22,12], [53,94,66]])
arr= np.argsort(sampleArray[1])
arr1 = sampleArray[:,arr]
print(arr1)

#CASE2
import numpy as np
sampleArray = np.array([[34,43,73], [82,22,12], [53,94,66]])
arr= np.argsort(sampleArray[:,1])
arr1 = sampleArray[arr,:]
print(arr1)


#Question 8

import numpy as np
sampleArray = np.array([[34,43,73], [82,22,12], [53,94,66]])
a = np.max(sampleArray, axis=0)
b = np.min(sampleArray, axis=1)
print(a)
print(b)


#Question 9

import numpy as np
sampleArray = np.array([[34,43,73], [82,22,12], [53,94,66]])
newColumn = np.array([[10,10,10]])
Array1 = np.delete(sampleArray, 1, axis=1)
arr = np.insert(Array1, 1, newColumn, axis=1)
print(sampleArray)
print(Array1)
print(arr)


#Question 10

import numpy as np
sampleArray = np.array([[34,43,73], [82,22,12], [53,94,66]])
newColumn = np.array([[10,10,10]])
Array1 = np.delete(sampleArray, 1, axis=1)
arr = np.insert(Array1, 1, newColumn, axis=1)
print(sampleArray)
print(Array1)
print(arr)
