import numpy as np

#init's an array with 4 0's (float64 0's)
h = np.zeros((4,))
h = np.zeros(4)

#init's a 4x4 array with 0's (float64 0's)
h = np.zeros([4,4])

#init's an array with numbers in ascending order. below is [0 1 2 3]
b = np.arange(4)
#same as above but [0. 1. 2. 3.] (float64)
b = np.arange(4.)

#both create an array with 4 random float64 (i think all less then 1)
c = np.random.random_sample(4)
c = np.random.rand(4)

#init's the array in the parenthesis 
d = np.array([5,4,3,2]) #int64
#be careful mixing datatypes, this array becomes [5. 4. 3. 2.] not [5. 4 3 2]
d = np.array([5.,4,3,2]) #float64

g = np.arange(10)
print(g[2]) #returns 2 the index value (scalar value)
print(g[2].shape) #returns () 
print(g[-1]) #returns 9
#g[10] is out of bounds


#vector slicing operations
a = np.arange(10)

print(f"a        =  {a}")

#access 5 consecutive elements (start:stop:step)
z = a[2:7:1];     print("a[2:7:1] = ", z)

# access 3 elements separated by two 
z = a[2:7:2];     print("a[2:7:2] = ", z)

# access all elements index 3 and above
z = a[3:];        print("a[3:]    = ", z)

# access all elements below index 3
z = a[:3];        print("a[:3]    = ",  z)

# access all elements
z = a[:];         print("a[:]     = ", z)


a = np.array([1,2,3,4])

#negates all of a
b = -a
print(b) 

#returns the sum of all elements in a (scalar)
b = np.sum(a)
print(b)

# returns the mean
b = np.mean(a)
print(b)

#returns the square of each element
b = a**2
print(b)

#returns a new arr with the sum of each paired element in a and b
a = np.array([ 1, 2, 3, 4])
b = np.array([-1,-2, 3, 4])
print(a + b)
#the vectors must be the same size 


a = np.array([1, 2, 3, 4])

# multiply a by a scalar
b = 5 * a 
print(b)
#scaling vectors ^^^

a = np.array([1, 2, 3, 4])
b = np.array([-1, 4, 3, 2])

#returns the dot product of 2 vectors
c = np.dot(a, b) # 24 in this case
#make sure to use np.dot instead of implementing the dot product with for loop because np.dot is vectorized

#.reshape with force a array into specified dimensions so long as it is possible
a = np.arange(6).reshape(-1, 2) #-1 represents the maximum possible rows given 2 columns (can also be: a = np.arange(6).reshape(3, 2))
#^^^ this becomes: ^^^
# [[0 1]
#  [2 3]
#  [4 5]]
print(a)





"""
print(c)
print(b.dtype)
print(a)
print(a.shape[0])
"""