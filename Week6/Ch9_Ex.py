import numpy as np


# Notes section
l = [1, 2, 3, 4, 5]
np_l = np.array(l)
print(l)
print(np_l)

two_dim_l = [[11,12],[21,22]]
np_2dl = np.array(two_dim_l)
print(two_dim_l)
print(np_2dl)

np_zeros = np.zeros((2,2))
print(np_zeros)

np_ones = np.ones((2,2))
print(np_ones)

np_ar = np.arange(1,10,3)
print(np_ar)

np_ls = np.linspace(1,10,3)
print(np_ls)

np_3d = np.ones((2,2,2))
print(np_3d)

nr_dim = len(np_3d.shape)
print(nr_dim)

nr_dim = np_3d.ndim
print(nr_dim)

np_arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(np_arr[0])
print(np_arr[-1])
print(np_arr[:5])
print(np_arr[7:])
print(np_arr[4:7])

twodim_nparr = np.array([[0,1],[2,3]])
print(twodim_nparr)
print(twodim_nparr[0,0])
print(twodim_nparr[0,:])
print(twodim_nparr[:,-1])

a = np.array([10,20,30,40,50])
print(a.mean())

print(a.max())
print(a.min())
print(a.argmax())
print(a.argmin())

b = np.array([1.0,2.0])
c = np.array([3.0,4.0])

print(b+c)
print(b-c)
print(2*b)
print(c/2)

print(b*c)
print(np.dot(b,c))
print(np.transpose(b))

d = np.array([1,2,3,3,3,4,4,5,6,6,6,6,6])
print(np.unique(d,return_counts=True))

# End of notes section

#Exercise 1
a = np.arange(2,10,2)
print(a)

#Exercise 2
a = np.array([[2,1],[6,3]])
print(a)

# Exercise 3
b = np.array([[1,0],[0,1]])
c = np.dot(a,b)
print(c,'\n')

# Exercise 4
print(sum(a[:]))




