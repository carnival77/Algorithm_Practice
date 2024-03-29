import sys
from collections import deque
input = sys.stdin.readline

class Shark:
    def __init__(self,x,y,size=2,feed=0):
        self.x=x
        self.y=y
        self.size=size
        self.feed=feed

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
ans=0

for i in range(n):
    for j in range(n):
        if a[i][j]==9:
            shark=Shark(i,j)
            a[i][j]=0

def bfs(shark):
    sx,sy,size=shark.x,shark.y,shark.size
    q=deque()
    q.append((sx,sy))
    d=[[-1] * n for _ in range(n)]
    d[sx][sy]=0
    cand=[]
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            ok=False
            eat=False
            # 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
            if 0<=nx<n and 0<=ny<n and d[nx][ny]==-1:
                if a[nx][ny]==0:
                    ok=True
                # 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
                elif a[nx][ny] < size:
                    ok=True
                    eat=True
                # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
                elif a[nx][ny]==size:
                    ok=True
                if ok:
                    q.append((nx,ny))
                    d[nx][ny]=d[x][y]+1
                    if eat:
                        cand.append([d[nx][ny],nx,ny])
    if len(cand)==0:
        return None
    cand.sort()
    return cand[0]

while True:
    target=bfs(shark)
    if target is None:
        break
    else:
        dist, tx, ty = target
        a[tx][ty] = 0
        shark.x, shark.y = tx, ty
        shark.feed += 1
        ans += dist
        if shark.feed == shark.size:
            shark.feed = 0
            shark.size += 1

print(ans)