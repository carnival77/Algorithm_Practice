import sys
from collections import deque
input=sys.stdin.readline

n,q=map(int,input().split())
N=2**n
a=[list(map(int,input().split())) for _ in range(N)]
ans1=0
ans2=0
N=2**n
ls=list(map(int,input().split()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def inBoard(nx,ny):
    if 0<=nx<N and 0<=ny<N:
        return True
    return False

def bfs(sx,sy):
    global visited

    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=True
    cnt=1

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and a[nx][ny]>0 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=True
                cnt+=1

    return cnt

for inx in range(q):
    l=ls[inx]
    L=2**l
    
    # 격자를 2L × 2L 크기의 부분 격자로 나눈다. 그 후, 모든 부분 격자를 시계 방향으로 90도 회전
    for x in range(0,N,L):
        for y in range(0,N,L):
            b=[[0]*L for _ in range(L)]
            for i in range(L):
                for j in range(L):
                    b[i][j]=a[x+i][y+j]
            b=list(map(list, zip(*b[::-1])))
            for i in range(L):
                for j in range(L):
                    a[x+i][y+j]=b[i][j]

    # 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다
    b=[row[:] for row in a]
    for x in range(N):
        for y in range(N):
            cnt=0
            for k in range(4):
                nx,ny=x+dx[k],y+dy[k]
                if inBoard(nx,ny) and a[nx][ny]>0:
                    cnt+=1
            if cnt<3 and a[x][y]>0:
                b[x][y]-=1
    a=b

for x in range(N):
    for y in range(N):
        if a[x][y]>0:
            ans1+=a[x][y]

visited=[[False]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if visited[x][y] or a[x][y]<=0:continue
        ans2=max(ans2,bfs(x,y))

print(ans1)
print(ans2)