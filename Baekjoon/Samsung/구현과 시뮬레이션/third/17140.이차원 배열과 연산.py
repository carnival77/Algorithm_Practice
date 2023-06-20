import sys
from collections import Counter
input=sys.stdin.readline

# C연산은 배열을 transpose 한 후 R연산을 적용 후 transpose 한 것과 같다.

r,c,k=map(int,input().split())
r-=1
c-=1
a=[list(map(int,input().split())) for _ in range(3)]
n,m=0,0

def check(time):
    if r<n and c<m:
        if a[r][c]==k:
            print(time)
            sys.exit(0)

def sorting(row):

    c = list(Counter(row).items())
    c.sort(key=lambda x: (x[1], x[0]))

    res = []
    for a, b in c:
        res.append(a)
        res.append(b)

    return res

def transpose(a):
    return list(map(list,zip(*a)))

def R(a):
    b=[]
    l=0
    n,m=len(a),len(a[0])
    for i in range(n):
        row=[]
        for j in range(m):
            if a[i][j]==0: continue
            row.append(a[i][j])
        sorted_row=sorting(row)
        b.append(sorted_row)
        l=max(l,len(sorted_row))
    l=min(100,l)
    c=[[0]*l for _ in range(n)]
    for i in range(n):
        for j in range(l):
            try:
                c[i][j]=b[i][j]
            except:
                pass

    return c

# def C():
#     global a
#
#     b = []
#     l = 0
#     for j in range(m):
#         col=[]
#         for i in range(n):
#             if a[i][j]==0: continue
#             col.append(a[i][j])
#         sorted_col = sorting(col)
#         b.append(sorted_col)
#         l = max(l, len(sorted_col))
#     l = min(100, l)
#     c = [[0] * l for _ in range(m)]
#     for i in range(m):
#         for j in range(l):
#             try:
#                 c[i][j]=b[i][j]
#             except:
#                 pass
#
#     a = transpose(c)

for time in range(101):
    n=len(a)
    m=len(a[0])
    check(time)
    if n>=m:
        a=R(a)
    else:
        a=transpose(R(transpose(a)))

print(-1)