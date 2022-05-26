# solution 1.
# 초기 맵을 bfs로 탐색하며 인접한 칸들끼리 그룹을 짓는다.
# 칸별 소속된 그룹의 번호는 group 배열, 그룹별 크기는 group_size 배열에 저장한다.
# bfs 후 다시 맵을 탐색하며 1인 칸에서 주변의 그룹들의 사이즈를 모두 더한다.

from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,input().split())

def bfs(sx,sy):
    q=deque()
    q.append((sx,sy))
    check[sx][sy]=True
    cnt=1
    g=len(group_size)
    group[sx][sy]=g
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and a[nx][ny]==0 and check[nx][ny]==False:
                q.append((nx,ny))
                check[nx][ny]=True
                cnt+=1
                group[nx][ny]=g
    group_size.append(cnt)

a=[]
group=[[0]*m for _ in range(n)]
group_size=[]
b=[[0]*m for _ in range(n)]
check=[[False]*m for _ in range(n)]
a = [list(map(int,list(input()))) for _ in range(n)]

for x in range(n):
    for y in range(m):
        if a[x][y]==0 and check[x][y]==False:
            bfs(x, y)

for x in range(n):
    for y in range(m):
        if a[x][y]==0:
            b[x][y]=0
            continue
        res=1
        near = set()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and a[nx][ny]==0:
                near.add(group[nx][ny])
        for g in near:
            res+=group_size[g]
        b[x][y]=res%10

for i in range(n):
    print("".join(map(str,b[i])))