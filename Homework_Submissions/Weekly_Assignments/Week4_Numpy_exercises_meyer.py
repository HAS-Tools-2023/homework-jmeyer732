#%%
# This script contains exercises on 
# manipulating arrays with numpy
import numpy as np


# %% Exercise 1: Working with a 1-D array:
x = np.arange(0, 3**3)
print(len(x))
print(x.shape)
print(x.dtype)

# 1.1 What is the length of x?
    # The length of x is 27

# Comprehension question is this an attribute or a method or a function of x? How do we know?
    # the length is an attribute or characteristic of x
#%%
# 1.2 Get the first value out of x and print it: 
x[0]
#%%
# 1.3. Get the last value out of x and print it?
x[-1]
x[26]
x[x.size-1]
#%%
# 1.4. Get the first 5 values and last 5 values out of x and print them?
print(x[0:5])
print(x[21:26])

# What if you dont know the length of the array?
array_length = len(x)
print(x[(array_length - 5):]) # the semi-colon with nothing after means until the end of the array, whatever that may mean.
#%%
# %% Exercise 2: Working with a 2-D array:
# 2.1 Get the first 9 values of x, and reshape them to a
#    3x3 matrix. Assign this matrix to the variable `y`
print(x)
y = np.reshape((x[0:9]), (3, 3))
print(y)

#%%
#BONUS show how you can do this with two lines of code and how you can do it with one line of code. 
    # with one line of code - shown above
    # with two lines of code - shown below
val = x[:9]
y = np.reshape(val, (3, 3))
print(y)

##Comprehension question: Is reshape a function, a method or an attribute of y?  How do we know? 
    # reshape is a function of the numpy library

#%%
# 2.2 Get the middle value out of y and print it?
y = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
])
y[1, 1]

#%%
# 2.3. Get the first row out of y and print it?
y[0, :]

# %%
# 2.4 If you save the first row of y to a new variable w what type of object is w? 
w = y[0,:]
print(w)
w.shape
    # w is a one-dimensional array

#%%
# 2.5 Get the first column out of y and print the lenght of this colum? (hint you will need to use the attribute 'size' to do this)
column = y[:,0]
np.size(column)

# BONUS: Try doing this two different ways. First where you save the column as a new variable and then get 
# its size (i.e. with two lines of code). And next where you combine thos commands into one line of code
columnagain = np.size(y[:,0])
print(columnagain)

#%% Exercise 3 Creating numpy arrays: 

# %%
# 3.1 use the np.arange function and the reshape method to create a numpy array with 3 rows and two columns 
# that has values 0-9
    # you can use 0 to 6 or create an array with random values from 0 to 9
nums = np.random.randint(10, size = 6)
print(nums)
len(nums)
np.reshape(nums, (3, 2))

# %%
# 3.2 use the np.ones function to create a 4 by 4 matrix with all ones 
fourbyfour = np.ones((4,4))
print(fourbyfour)

# %% 
# 3.3 Now modify the matrix you created in the last exercise to make the values all 4's   
# (Hint: you could do this with either addition or multiplication)
allfours1 = np.full((4, 4), 4)
print(allfours1)
# or
allfours2 = fourbyfour * 4
print(allfours2)

#%% Exercise 4:  using the axis argument
z=np.arange(20).reshape((5,4))

# 4.1 Use 'sum' to print the total of z
print(z.sum())
# or
print(np.sum(z))

#Comprehension question -- is 'sum' a function a method or an attribute?  
    # in the first example, sum is a method
    # in the second example, sum is a function of the numpy library

#%%
# 4.2. Print the sum along the first dimension of z?
print(z)
firstdimsum = np.sum(np.concatenate(np.vsplit(z, 5)))
print(firstdimsum)

## Comprehension question -- is the 'first dimension' the rows or the columns of z? 
    # the first dimension is considered the length of array z

# %% 
# 4.3 How many elements does your answer to exercise 4.2 have? (i.e. how many numberd did you get back?)
    # it has 5 arrays and 1 sum element, as the matrix needed to be unstacked, sub-arrays added onto
    # one another, and then the sum of all integers within the one-dimensional array calculated.

# How does this compare to the shape of z? 
    # the shape of matrix z is a 2-dimensional 4 by 5 (4 rows by 5 columns) and the shape of array z 
    # is one-dimensional 1 by 5 (1 row by 5 arrays). However, technically, the sum is the addition of 
    # all integers from all 5 sub-arrays within array z. 