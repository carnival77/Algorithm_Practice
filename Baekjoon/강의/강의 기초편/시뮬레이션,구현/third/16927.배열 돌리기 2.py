import sys
from collections import deque
input=sys.stdin.readline

n,m,r=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

for k in range(min(n,m)//2):
    q=deque()
    for i in range(k,m-1-k):
        q.append(a[k][i])
    for i in range(k,n-1-k):
        q.append(a[i][m-1-k])
    for i in range(m-1-k,k,-1):
        q.append(a[n-1-k][i])
    for i in range(n-1-k,k,-1):
        q.append(a[i][k])
    q.rotate(-1*r)
    for i in range(k,m-1-k):
        a[k][i]=q.popleft()
    for i in range(k,n-1-k):
        a[i][m-1-k]=q.popleft()
    for i in range(m-1-k,k,-1):
        a[n-1-k][i]=q.popleft()
    for i in range(n-1-k,k,-1):
        a[i][k]=q.popleft()

for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()