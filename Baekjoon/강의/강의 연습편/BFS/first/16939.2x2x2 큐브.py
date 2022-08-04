#!/usr/bin/env Python
# coding=utf-8
a=[0]+list(map(int,input().split()))

def check(a):
    for i in range(6):
        for j in range(2,5):
            if a[i*4+1]!=a[i*4+j]:
                return False
    return True

def lu(a):
    b=a[:]
    b[1],b[5],b[9],b[24]=b[5],b[9],b[24],b[1]
    b[3],b[7],b[11],b[22]=b[7],b[11],b[22],b[3]
    return b

def ld(a):
    return lu(lu(lu(a[:])))

def ru(a):
    b=a[:]
    b[2],b[6],b[10],b[23]=b[6],b[10],b[23],b[2]
    b[4],b[8],b[12],b[21]=b[8],b[12],b[21],b[4]
    return b

def rd(a):
    return ru(ru(ru(a[:])))

def ul(a):
    b=a[:]
    b[13],b[5],b[17],b[21]=b[5],b[17],b[21],b[5]
    b[14],b[6],b[18],b[22]=b[6],b[18],b[22],b[14]
    return b

def ur(a):
    return ul(ul(ul(a[:])))

def dl(a):
    b=a[:]
    b[15],b[7],b[19],b[23]=b[7],b[19],b[23],b[15]
    b[16],b[8],b[20],b[24]=b[8],b[20],b[24],b[16]
    return b

def dr(a):
    return dl(dl(dl(a)))

def fl(a):
    b=a[:]
    b[3],b[17],b[10],b[16]=b[17],b[10],b[16],b[3]
    b[4],b[19],b[9],b[14]=b[19],b[9],b[14],b[4]
    return b

def fr(a):
    return fl(fl(fl(a[:])))

def bl(a):
    b=a[:]
    b[1],b[18],b[12],b[15]=b[18],b[12],b[15],b[1]
    b[2],b[20],b[11],b[13]=b[20],b[11],b[13],b[2]
    return b

def br(a):
    return bl(bl(bl(a)))

if check(lu(a)) or check(ld(a)) or check(ru(a)) or check(rd(a)) or check(ul(a)) or check(ur(a)) or check(dl(a)) or check(dr(a)) or check(fl(a)) or check(fr(a)) or check(bl(a)) or check(br(a)):
    print(1)
else:
    print(0)