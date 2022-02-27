from base import *

# FUNGSI UTAMA, untuk mengembalikan convex hull dari kumpulan data 2D
# (kumpulan titik-titik)
def myConvexHull(bucket):
    # inisialisasi hull sebagai array kosong
    hull = []
    # mengurutkan points berdasarkan posisi-x, jika sama lanjut diurutkan berdasar posisi-y
    bSorted = sorted(bucket,key=lambda x: (x[0],x[1]))
    # assign nilai titik p1 dan pn 
    p1 = bSorted[0]
    pn = bSorted[len(bSorted)-1]
    
    # segmentasi daerah, menjadi bagian kiri/atas dan kanan/bawah
    sLeft = fillLeftPart(p1,pn,bucket)
    sRight = fillLeftPart(pn,p1,bucket)
    # melakukan rekursi untuk mendapatkan titik-titik terluar dari kumpulan data 2D
    # pada bagian kiri/atas dan kanan/bawah
    leftHull = convexHullLeft(p1,pn,sLeft)
    # rightHull menggunakan fungsi convexHullLeft juga, 
    # hanya saja penggunaan parameternya berlawanan
    rightHull = convexHullLeft(pn,p1,sRight)

    # mengisi array hull dengan titik-titik terluar dari kumpulan data 2D
    hull.append([p1[0],p1[1]])
    hull += leftHull 
    hull.append([pn[0],pn[1]])
    hull += rightHull
    hull = convertUnique(hull)

    # menemukan index dari titik-titik terluar yang didapat
    # agar dapat dilakukan plotting
    hullConstructor = buildHull(hull,bucket)

    return hullConstructor
