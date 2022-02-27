import numpy as np
# import pandas as pd 
# import matplotlib.pyplot as plt

hullTemp = []

def convert(arr):
    temp = []
    for i in range(len(arr)):
        temp.append(arr[i])
    return temp

def detResult(p1, p2, px):
    det = p1[0]*p2[1] + px[0]*p1[1] + p2[0]*px[1] - px[0]*p2[1] - p2[0]*p1[1] - p1[0]*px[1]
    return det

def fillLeftPart(p1, p2, points):
    sTemp = []
    for i in range(len(points)):
        det = detResult(p1,p2,points[i])
        if det > 0:
            sTemp.append(points[i])
    return sTemp

def fillRightPart(p1, p2, points):
    sTemp = []
    for i in range(len(points)):
        det = detResult(p1,p2,points[i])
        if det < 0:
            sTemp.append(points[i])
    return sTemp

def distance(p1,p2,px):
    return abs((p2[0]-p1[0])*(p1[1]-px[1]) - (p1[0]-px[0])*(p2[1]-p1[1])) / np.sqrt(np.square(p2[0]-p1[0]) + np.square(p2[1]-p1[1]))

def find_pMax(p1,p2,points):
    temp = convert(points)
    pMax = temp[0]
    dMax = distance(p1,p2,temp[0])
    for i in range(len(temp)):
        d = distance(p1,p2,temp[i])
        if (d > dMax):
            dMax = d
            pMax = temp[i]
    return pMax    

# def convexHullLeft(p1, p2, left):
#     global hullTemp    
#     if (len(left) != 0):
#         # cari pMax
#         pMax = find_pMax(p1, p2, left)
#         # cari leftL dan leftR
#         leftL = fillLeftPart(p1, pMax, left)
#         leftR = fillLeftPart(pMax, p2, left)
#         # tambah pMax ke hull
#         if (pMax not in hullTemp):
#             hullTemp.append(pMax)
#         # convex hull leftL,p1,pMax
#         convexHullLeft(p1, pMax, leftL)
#         # convex hull leftR,pMax,p2
#         convexHullLeft(pMax, p2, leftR)
#     return # hullTemp

# def convexHullRight(p1, p2, right):
#     global hullTemp
#     if (len(right) != 0):
#         # cari pMax
#         pMax = find_pMax(p1,p2,right)
#         # cari rightL dan rightR
#         rightL = fillRightPart(p1,pMax,right)
#         rightR = fillRightPart(pMax,p2,right)
#         # tambah pMax ke hull
#         if (pMax not in hullTemp):
#             hullTemp.append(pMax)
#         # convex hull rightL,p1,pMax
#         convexHullRight(p1, pMax, rightL)
#         # convex hull rightR,pMax,p2
#         convexHullRight(pMax, p2, rightR)
#     return # hullTemp

# def convexHull():

def myConvexHull(bucket):
    global hullTemp
    if(len(bucket) > 0):
        bSorted = sorted(bucket,key=lambda x: (x[0],x[1]))
        p1 = bSorted[0]
        pn = bSorted[len(bSorted)-1]
        hullTemp.append(p1)
        hullTemp.append(pn)

        sLeft = fillLeftPart(p1,pn,bucket)
        sRight = fillRightPart(p1,pn,bucket)
        print(sLeft)
        print(sRight)
        # convexHullLeft(p1,pn,sLeft)
        # convexHullRight(p1,pn,sRight)

    # return hullTemp

# bucket = [
#     [1.,1.], [5.,5.], [2.,7.], [3.,7],[4.,6.], [2,-1], [3,0], [4,-2]
# ]
# hull = myConvexHull(bucket)
# print(hull)
