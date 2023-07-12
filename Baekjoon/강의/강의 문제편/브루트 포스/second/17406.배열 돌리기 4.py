import sys
from collections import deque
from itertools import permutations
input=sys.stdin.readline

n,m,K=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

cand=[]
for _ in range(K):
    cand.append(list(map(int,input().split())))

ans=int(1e9)

def rotate_90_clockwise(a,n,m):
    for k in range(min(n, m) // 2):
        q = deque()
        for i in range(k, m - 1 - k):
            q.append(a[k][i])
        for i in range(k, n - 1 - k):
            q.append(a[i][m - 1 - k])
        for i in range(m - 1 - k, k, -1):
            q.append(a[n - 1 - k][i])
        for i in range(n - 1 - k, k, -1):
            q.append(a[i][k])
        q.rotate(1)
        for i in range(k, m - 1 - k):
            a[k][i] = q.popleft()
        for i in range(k, n - 1 - k):
            a[i][m - 1 - k] = q.popleft()
        for i in range(m - 1 - k, k, -1):
            a[n - 1 - k][i] = q.popleft()
        for i in range(n - 1 - k, k, -1):
            a[i][k] = q.popleft()
    return a

for perm in permutations(cand,K):
    b=[row[:] for row in a]
    for r,c,s in perm:
        x1,y1=r-s-1,c-s-1
        x2,y2=r+s-1,c+s-1
        n=x2-x1+1
        m=y2-y1+1
        part=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                part[i][j]=b[x1+i][y1+j]
        part=rotate_90_clockwise(part,n,m)
        for i in range(n):
            for j in range(m):
                b[x1 + i][y1 + j]=part[i][j]
    for row in b:
        ans=min(ans,sum(row))

print(ans)