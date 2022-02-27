import numpy as np
from numpy.linalg import *

# l=[[1,4],[2,7],[10,1],[1,2],[10,6],[2,1]]
# lSort = sorted(l,key=lambda x: (x[0],x[1]))
# print(lSort)
# print(lSort[0], lSort[len(lSort)-1])

a1 = 0
a2 = 5
b1 = 5
b2 = 0
c1 = -1
c2 = 0
det = a1*b2 + c1*a2 + b1*c2 - c1*b2 - b1*a2 - a1*c2
# print(det)

# a = [0,0]
# b = [5,0]
# c = [3,6.7]
# d = abs((b[0]-a[0])*(a[1]-c[1]) - (a[0]-c[0])*(b[1]-a[1])) / np.sqrt(np.square(b[0]-a[0]) + np.square(b[1]-a[1]))
# print(d)

