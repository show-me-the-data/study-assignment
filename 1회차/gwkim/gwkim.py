import numpy as np

# 수정사항!
index = 1

# 1.Write a NumPy program to get the numpy version and show numpy build configuration
print(index, "번 넘파이 버전 : ", np.__version__)
print()
index += 1

# 2. Write a NumPy program to  get help on the add function
print(index,"번")
print(np.info(np.add))
print()
index += 1

# 3. Write a NumPy program to test whether none of the elements of a given array is zero.
print(index,"번")
x = np.array([1, 2, 3, 4])
print(np.all(x))
x = np.array([0, 2, 3, 4])
print(np.all(x))
print()
index += 1

# 4. Write a NumPy program to test whether any of the elements of a given array is non-zero
print(index,"번")
x = np.array([1, 0, 3, 4])
print(np.any(x))
x = np.array([0, 0, 0, 0])
print(np.any(x))
print()
index += 1

# 5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number). 
print(index,"번")
x = np.array([np.nan, 0, 3, 4])
print(np.isfinite(x))
x = np.array([0, 0, np.inf, 0])
print(np.isfinite(x))
print()
index += 1

# 6. Write a NumPy program to test element-wise for positive or negative infinity.
print(index,"번")
x = np.array([np.nan, 0, 3, 4])
print(np.isinf(x))
x = np.array([0, 0, np.inf, 0])
print(np.isinf(x))
print()
index += 1

# 7. Write a NumPy program to test element-wise for NaN of a given array. 
print(index,"번")
x = np.array([np.nan, 0, 3, 4])
print(np.isnan(x))
x = np.array([0, 0, np.inf, 0])
print(np.isnan(x))
print()
index += 1

# 8. Write a NumPy program to test element-wise for complex number, 
# real number of a given array. Also test whether a given number is a scalar type or not.
print(index,"번")
x = np.array([np.nan, 1+2j, 3, 4])
print(np.iscomplex(x))
print(np.isreal(x))
print(np.isscalar(x))
print()
index += 1

# 9. Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.
print(index,"번")
print(np.allclose([1e10,1e-7], [1.00001e10,1e-8]))
print(np.allclose([1e10,1e-8], [1.00001e10,1e-9]))
print(np.allclose([1e10,1e-8], [1.0001e10,1e-9]))
print(np.allclose([1.0, np.nan], [1.0, np.nan]))
print(np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True))
print()
index += 1

# 10. Write a NumPy program to create an element-wise 
# comparison (greater, greater_equal, less and less_equal) of two given arrays.
print(index,"번")
x = np.array([1, 2, 4, 5])
y = np.array([9, 2, 2, 4])
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print()
index += 1

# 11. Write a NumPy program to create an 
# element-wise comparison (equal, equal within a tolerance) of two given arrays.
print(index,"번")
print(np.equal(x, y))
print(np.allclose(x, y))
print()
index += 1

# 12. Write a NumPy program to create an array with the values 1, 7, 13, 105 
# and determine the size of the memory occupied by the array.
print(index,"번")
x = np.array([1, 7, 13, 105])
print(x.size * x.itemsize)
print()
index += 1

# 13. Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.
print(index,"번")
print(np.zeros(10))
print(np.ones(10))
print(np.ones(10) * 5)
print()
index += 1

# 14. Write a NumPy program to create an array of the integers from 30 to70.
print(index,"번")
print(np.arange(30, 71))
print()
index += 1

# 15. Write a NumPy program to create an array of all the even integers from 30 to 70.
print(index,"번")
print(np.arange(30, 71, 2))
print()
index += 1

# 16. Write a NumPy program to create a 3x3 identity matrix.
print(index,"번")
print(np.identity(3))
print()
index += 1

# 17. Write a NumPy program to generate a random number between 0 and 1.
print(index,"번")
print(np.random.normal(0, 1, 1))
print()
index += 1

# 18. Write a NumPy program to generate an array of 
# 15 random numbers from a standard normal distribution.
print(index,"번")
print(np.random.normal(0, 1, 15))
print()
index += 1

# 19. Write a NumPy program to create a vector with values 
# ranging from 15 to 55 and print all values except the first and last.
print(index,"번")
print(np.arange(15, 56))
print(np.arange(15, 56)[1:-1])
print()
index += 1

# 20. Write a NumPy program to create a 3X4 array using and iterate over it.
print(index,"번")
a = np.arange(1, 13).reshape(3, 4)
print(a)
for ele in np.nditer(a):
    print(ele, end=" ")
print()
print()
index += 1

# 21. Write a NumPy program to create a vector of 
# length 10 with values evenly distributed between 5 and 50
print(index,"번")
a = np.linspace(5, 49) 
print(a)
index += 1
print()

# 22. Write a NumPy program to create a vector with values 
# from 0 to 20 and change the sign of the numbers in the range from 9 to 15
print(index,"번")
a = np.arange(0, 21)
a[9:17] =- a[9:17]
print(a)
index += 1
print()

# 23. Write a NumPy program to create a vector of length 5
#  filled with arbitrary integers from 0 to 10
print(index,"번")
a = np.random.randint(0, 11, 5)
print(a)
index += 1
print()

# 24. Write a NumPy program to multiply the values of two given vectors.
print(index,"번")
a = np.arange(10)
b = np.arange(10)
print(a * b)
index += 1
print()

# 25. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21. 
print(index,"번")
a = np.arange(10, 22).reshape(3, 4)
print(a)
index += 1
print()

# 26. Write a NumPy program to find the number of rows and columns of a given matrix.
print(index,"번")
a = np.arange(10, 22).reshape(3, 4)
print(a.shape)
index += 1
print()

# 27. Write a NumPy program to create a 3x3 identity matrix, 
# i.e. diagonal elements are 1, the rest are 0.
print(index,"번")
a = np.eye(3)
print(a)
index += 1
print()

# 28. Write a NumPy program to create a 10x10 matrix, 
# in which the elements on the borders will be equal to 1, and inside 0. 
print(index,"번")
a = np.ones(100).reshape(10, 10)
a[1:-1, 1:-1] = 0
print(a)
index += 1
print()

# 29. Write a NumPy program to create a 5x5 zero matrix 
# with elements on the main diagonal equal to 1, 2, 3, 4, 5.
print(index,"번")
a = np.ones(100).reshape(10, 10)
a[1:-1, 1:-1] = 0
print(a)
index += 1
print()

# 30. Write a NumPy program to create a 4x4 matrix 
# in which 0 and 1 are staggered, with zeros on the main diagonal. 
print(index,"번")
a = np.zeros((4,4))
a[::2, 1::2] = 1
a[1::2, ::2] = 1
print(a)
index += 1
print()

# 31. Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
print(index,"번")
a = np.random.normal(0, 1, 27).reshape(3, 3, 3)
print(a)
index += 1
print()

# 32. Write a NumPy program to compute sum of all elements, 
# sum of each column and sum of each row of a given array.
print(index,"번")
a = np.array([[0,1],[2,3]])
print(np.sum(a))
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
index += 1
print()

# 33. Write a NumPy program to compute the inner product of two given vectors
print(index,"번")
a = np.random.randint(0, 10, 4)
b = np.random.randint(0, 10, 4)
print(np.dot(a, b))
index += 1
print()

# 34. Write a NumPy program to add a vector to each row of a given matrix.
print(index,"번")
a = np.random.randint(0, 10, 4).reshape(2, 2)
b = np.random.randint(0, 10, 4).reshape(2, 2)
print(np.add(a, b))
index += 1
print()

# 41. Write a NumPy program to convert numpy dtypes to native python types.
print(index,"번")
x = np.float32(0)
print(type(x))
print(type(x.item()))
index += 1
print()
