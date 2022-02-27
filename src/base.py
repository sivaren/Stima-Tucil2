import numpy as np

# Untuk membuat values dalam array menjadi unik, tidak ada duplikat
def convertUnique(arr):
    temp = []
    for i in range(len(arr)):
        if(arr[i] not in temp):
            temp.append([arr[i][0],arr[i][1]])
    return temp

# Untuk menghasilkan nilai determinan dari 3 titik
def detResult(p1, p2, px):
    det = p1[0]*p2[1] + px[0]*p1[1] + p2[0]*px[1] - px[0]*p2[1] - p2[0]*p1[1] - p1[0]*px[1]
    return det

# Untuk mancari jarak dari suatu titik ke garis
def distance(p1,p2,px):
    return abs((p2[0]-p1[0])*(p1[1]-px[1]) - (p1[0]-px[0])*(p2[1]-p1[1])) / np.sqrt(np.square(p2[0]-p1[0]) + np.square(p2[1]-p1[1]))

# Untuk mendapatkan himpunan titik-titik bagian kiri/atas garis pembatas
def fillLeftPart(p1, p2, points):
    sTemp = []
    if(len(points) > 0):
        for point in points:
            det = detResult(p1,p2,point)
            if det > 0:
                x = point[0]
                y = point[1]
                sTemp.append([x,y])
    return sTemp

# Untuk mendapatkan himpunan titik-titik bagian kanan/bawah garis pembatas
def fillRightPart(p1, p2, points):
    sTemp = []
    if(len(points) > 0):
        for point in points:
            det = detResult(p1,p2,point)
            if det < 0:
                x = point[0]
                y = point[1]
                sTemp.append([x,y])
    return sTemp

# Untuk mencari titik terjauh dari suatu garis
def find_pMax(p1,p2,points):
    pMax = points[0]
    dMax = distance(p1,p2,points[0])
    for i in range(len(points)):
        d = distance(p1,p2,points[i])
        if (d > dMax):
            dMax = d
            pMax = points[i]
    return [pMax[0],pMax[1]]        

# Untuk mendapatkan titik-titik terluar dari suatu himpunan titik-titik
# terhadap suatu garis pembatas
def convexHullLeft(p1, p2, left):
    if (len(left) == 0):
        return [[p1[0],p1[1]],[p2[0],p2[1]]]
    elif(len(left) == 1):
        return left
    else:
        # cari pMax
        pMax = find_pMax(p1, p2, left)
        # cari leftL dan leftR
        leftL = fillLeftPart(p1, pMax, left)
        leftR = fillLeftPart(pMax, p2, left)
        # rekursif convex hull part kiri dan kanan
        leftHull = convexHullLeft(p1, pMax, leftL)
        rightHull = convexHullLeft(pMax, p2, leftR)
        return leftHull + rightHull

# Untuk mendapatkan index suatu point yang terletak pada bucket
def getIdx(point, bucket):
    for i in range(len(bucket)):
        if(point[0] == bucket[i][0] and point[1] == bucket[i][1]):
            return i

# Untuk mendapatkan index dari titik-titik terluar yang telah ditemukan
def buildHull(points,bucket):
    temp = []
    for i in range(len(points)-1):
        idx1 = getIdx(points[i],bucket)
        idx2 = getIdx(points[i+1],bucket)
        temp.append([idx1, idx2])
    idx1 = getIdx(points[len(points)-1],bucket)
    idx2 = getIdx(points[0],bucket)
    temp.append([idx1, idx2])
    return temp
