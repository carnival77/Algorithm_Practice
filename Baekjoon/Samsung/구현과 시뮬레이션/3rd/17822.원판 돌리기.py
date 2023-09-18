import sys
from collections import deque

input=sys.stdin.readline

n,m,t=map(int,input().split())

a=[] # 원판의 수는 양의 정수. 수가 없는 경우는 0
for _ in range(n):
    q=deque(list(map(int,input().split())))
    a.append(q)

ans=0

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def check():
    for x in range(n):
        for y in range(m):
            if a[x][y]>0:
                return True
    return False

def inBoard(nx):
    if 0<=nx<n:
        return True
    return False

# 인접하면서 수가 같은 칸을 모두 찾아 삭제 대상에 포함시킨다.
def bfs(sx,sy,delete):

    ok=False
    q=deque()
    q.append((sx,sy))
    visited=[[False]*m for _ in range(n)]
    visited[sx][sy]=True

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            # 각 원판의 양 끝은 서로를 탐색할 수 있다.
            if ny<0:
                ny=m-1
            elif ny>=m:
                ny=0
            # 1번 원판의 안 쪽이나 제일 큰 원판의 바깥 쪽, 그리고 수가 없거나(0) 이미 탐색한 칸은 탐색하지 않는다.
            if not inBoard(nx) or a[nx][ny]==0 or visited[nx][ny]:
                continue
            # 인접하면서 수가 같은 칸을 찾았으면, 찾은 칸을 삭제 대상으로 표시하고, 찾은 인접한 같은 수의 위치에서 또다른 인접한 같은 수를 찾는다.
            if a[nx][ny]==a[sx][sy]:
                ok=True
                visited[nx][ny]=True
                delete[nx][ny]=True
                q.append((nx,ny))

    if ok:
        delete[sx][sy]=True

    return [ok,delete]

def process():
    global a

    ok=False # 인접하면서 같은 수의 존재 여부
    delete=[[False]*m for _ in range(n)] # 삭제 대상

    if check(): # 원판에 수가 남아 있으면
        for x in range(n):
            for y in range(m):
                if a[x][y]==0 or delete[x][y]:
                    continue
                # 해당 칸이 비어있지 않고(0이 아님), 이미 삭제 대상에 포함되어 있지 않으면
                res=bfs(x, y,delete) # 인접하면서 수가 같은 칸을 모두 찾아 삭제 대상에 포함시킨다.
                delete=res[1]
                # 인접하면서 같은 수 그룹이 하나라도 있으면 ok=True
                if not ok:
                    ok=res[0]

    # 인접하면서 같은 수를 모두 지운다.
    if ok:
        for x in range(n):
            for y in range(m):
                if delete[x][y]:
                    a[x][y]=0
    # 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
    else:
        tot,cnt=0,0
        for x in range(n):
            for y in range(m):
                if a[x][y]>0:
                    tot+=a[x][y]
                    cnt+=1
        if cnt>0:
            avg=tot/cnt
            for x in range(n):
                for y in range(m):
                    if a[x][y]==0:
                        continue
                    if a[x][y]>avg:
                        a[x][y]-=1
                    elif a[x][y]<avg:
                        a[x][y]+=1

for _ in range(t):
    x,d,k=map(int,input().split())

    # 회전
    # 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
    for i in range(1,n+1):
        if i%x==0:
            if d==0:
                a[i-1].rotate(k)
            else:
                a[i-1].rotate(-k)

    # 작업
    process()

for x in range(n):
    for y in range(m):
        ans+=a[x][y]
print(ans)