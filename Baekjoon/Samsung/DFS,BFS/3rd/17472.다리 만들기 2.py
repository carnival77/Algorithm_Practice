from collections import deque

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 0은 바다, 1은 땅
b=[[0]*m for _ in range(n)] # 섬 맵

dx=[-1,0,1,0]
dy=[0,1,0,-1]

ans=0
v=0 # 섬 개수
parent=[] # 섬(노드)

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def bfs(sx,sy,visit,no):
    global b

    q=deque()
    q.append((sx,sy))
    visit[sx][sy]=True
    b[sx][sy]=no

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visit[nx][ny] and a[nx][ny]==1:
                q.append((nx,ny))
                visit[nx][ny]=True
                b[nx][ny]=no

    return visit

def init():
    global parent,v

    visit=[[False]*m for _ in range(n)]
    no=0
    for x in range(n):
        for y in range(m):
            if a[x][y]==1 and not visit[x][y]:
                no += 1
                visit=bfs(x,y,visit,no)

    v = no  # 섬 개수
    parent = [0] * (v + 1)

    # 부모 노드 초기화
    for i in range(1, v + 1):
        parent[i] = i

def getEdges():

    edges=[]

    for i in range(n):
        for j in range(m):
            if a[i][j]==0:continue
            x1=b[i][j]
            for k in range(4):
                x, y = i, j
                dist = 0
                while True:
                    nx,ny=x+dx[k],y+dy[k]
                    if not inBoard(nx,ny) or b[nx][ny]==x1:
                        break
                    if a[nx][ny]==0:
                        x,y=nx,ny
                        dist+=1
                    elif a[nx][ny]==1 and b[nx][ny]!=x1:
                        if dist>=2:
                            x2=b[nx][ny]
                            edges.append([dist,x1,x2])
                        break
    return edges

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def check():

    for i in range(1,v+1):
        if parent[i]!=1:
            return False

    return True

ok=False
# 섬 파악
init()
# 가능한 다리 파악
edges=getEdges()
edges.sort()
# 최소비용으로 섬 연결
for cost,x,y in edges:
    x1=find_parent(parent,x)
    x2=find_parent(parent,y)
    if x1!=x2:
        union_parent(parent,x,y)
        ans+=cost
        for i in range(2,v+1):
            if parent[i]==x2:
                union_parent(parent,x1,i)
    # 섬 모두 연결
    ok=check()
    if ok:
        print(ans)
        break
if not ok:
    print(-1)