import sys
from itertools import permutations
from collections import deque

input=sys.stdin.readline

n,m,K=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=int(1e9)

data=[list(map(int,input().split())) for _ in range(K)]

def rotateMatrix(a,r,c,s):
    
    l=2*s+1
    x1=r-s-1
    x2=r+s-1
    y1=c-s-1
    y2=c+s-1
    
    for k in range((l-1)//2+1):
        q=deque()
        for y in range(y1 + k, y2 - k):
            q.append(a[x1+k][y])
        for x in range(x1+k,x2-k):
            q.append(a[x][y2-k])
        for y in range(y2-k,y1+k,-1):
            q.append(a[x2-k][y])
        for x in range(x2-k,x1+k,-1):
            q.append(a[x][y1+k])
        q.rotate(1)
        for y in range(y1 + k, y2 - k):
            a[x1+k][y]=q.popleft()
        for x in range(x1+k,x2-k):
            a[x][y2-k]=q.popleft()
        for y in range(y2-k,y1+k,-1):
            a[x2-k][y]=q.popleft()
        for x in range(x2-k,x1+k,-1):
            a[x][y1+k]=q.popleft()

    return a

def process(perm):

    res=int(1e9)
    b=[row[:] for row in a]
    for r,c,s in perm:
        b=rotateMatrix(b,r,c,s)

    for row in b:
        res=min(res,sum(row))

    return res

for perm in permutations(data):
    perm=list(perm)
    ans=min(ans,process(perm))

print(ans)