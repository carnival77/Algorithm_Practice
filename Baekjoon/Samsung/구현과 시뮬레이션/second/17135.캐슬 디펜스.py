import sys
from collections import deque
from itertools import combinations
input=sys.stdin.readline

n,m,d=map(int,input().split())
b=[list(map(int,input().split())) for _ in range(n)]
b.append([2]*m)
arr=[i for i in range(m)]
ans=0

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def check():
    for x in range(n):
        for y in range(m):
            if a[x][y]==1:
                return True
    return False

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def bfs(sy,d):
    sx=n
    q=deque()
    q.append((sx,sy))
    dist=[[-1]*m for _ in range(n+1)]
    dist[sx][sy]=0
    res=[]

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if not inBoard(nx,ny) or dist[nx][ny]!=-1 or abs(nx-sx)+abs(ny-sy)>d or a[nx][ny]==2: continue
            q.append((nx,ny))
            dist[nx][ny]=dist[x][y]+1
            if a[nx][ny]==1:
                res.append((dist[nx][ny],nx,ny))

    if len(res)==0:
        return (-1,-1)
    elif len(res)>1:
        res.sort(key=lambda x:(x[0],x[2]))
    return res[0][1:]

def move():
    global a

    a[n-1]=[0]*m
    for i in range(n-1,0,-1):
        a[i]=a[i-1]
    a[0]=[0]*m

# 궁수 배치하는 모든 경우의 수
for comb in combinations(arr,3):
    a=[row[:] for row in b]
    res=0 # 이번 배치에서의 점수
    # 모든 적이 격자판에서 제외되면 게임 종료
    while check():
        # 궁수 공격
        tgs=set() # 사라질 적의 위치
        for i in list(comb):
            tg=bfs(i,d)
            if tg!=(-1,-1):
                tgs.add(tg)
        for x,y in tgs:
            a[x][y]=0
            res+=1
        # 적 아래로 한 칸 이동
        move()
    ans=max(ans,res)

print(ans)