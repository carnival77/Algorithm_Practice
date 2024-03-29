import sys
from collections import deque
input=sys.stdin.readline

n=int(input())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

a=[]
sx,sy,size,cnt=0,0,2,0
for i in range(n):
    row=list(map(int,input().split()))
    for j in range(len(row)):
        if row[j]==9:
            sx,sy=i,j
    a.append(row)
a[sx][sy]=0

time=0

def possible():
    for i in range(n):
        for j in range(n):
            if 0<a[i][j]<size:
                return True
    return False

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def bfs():
    global a,time,size,cnt,sx,sy

    q=deque()
    q.append((sx,sy))
    d=[[-1]*n for _ in range(n)]
    d[sx][sy]=0
    cand = []

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if not inBoard(nx,ny) or d[nx][ny]!=-1 or a[nx][ny]>size: continue
            q.append((nx,ny))
            d[nx][ny]=d[x][y]+1
            if 0<a[nx][ny]<size:
                cand.append((d[nx][ny],nx,ny))

    if len(cand)==0:
        print(time)
        sys.exit(0)
    cand.sort()
    tg=cand[0]
    time+=tg[0]
    tx,ty=tg[1:]
    a[tx][ty]=0
    sx,sy=tx,ty
    cnt += 1
    if cnt==size:
        cnt=0
        size+=1

while True:
    if not possible():
        print(time)
        sys.exit(0)
    bfs()