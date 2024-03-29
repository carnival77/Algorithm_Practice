import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
edges=[]
v=1
ans=0
parent=[]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def bfs1(sx,sy,no):
    global board

    q=deque()
    q.append((sx,sy))
    visit=[[False]*m for _ in range(n)]
    visit[sx][sy]=True
    board[sx][sy]=no
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visit[nx][ny] and board[nx][ny]==1:
                q.append((nx,ny))
                visit[nx][ny]=True
                board[nx][ny]=no

def init():
    global v

    no=2
    for x in range(n):
        for y in range(m):
            if board[x][y]==1:
                bfs1(x,y,no)
                v+=1
                no+=1

def bfs2(sx,sy,no):
    res=[]
    d=[[-1]*m for _ in range(n)]
    d[sx][sy]=0
    for k in range(4):
        q=deque()
        q.append((sx,sy))
        while q:
            x,y=q.popleft()
            nx,ny=x+dx[k],y+dy[k]
            if not inBoard(nx,ny):
                continue
            if board[nx][ny]==no:
                break
            elif board[nx][ny]==0:
                q.append((nx,ny))
                d[nx][ny]=d[x][y]+1
            else:
                if d[x][y]>=2:
                    res.append((d[x][y],no,board[nx][ny]))
    return res

def makeBridge():
    global edges

    for x in range(n):
        for y in range(m):
            if board[x][y]==0:
                continue
            for edge in bfs2(x,y,board[x][y]):
                edges.append(edge)

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 찾기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def makeMST():
    global ans,parent

    parent=[0]*(v+1)
    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(2, v + 1):
        parent[i] = i
    edges.sort()

    for edge in edges:
        cost,a,b=edge
        parent_a=find_parent(parent,a)
        parent_b=find_parent(parent,b)
        if parent_a!=parent_b:
            union_parent(parent,a,b)
            ans+=cost
            for i in range(2,v+1):
                if parent[i]==parent_b:
                    union_parent(parent,parent_a,i)

# 1. 섬 파악
init()

# 2. 다리 연결 후보 선정
makeBridge()

# 3. 최소 비용으로 모든 섬 연결 - 최소 스패닝 트리 구성
makeMST()

# 모든 섬 연결 가능하면 최소 비용 출력
ok=False
for i in parent[2:]:
    # 아니면 -1 출력
    if i!=2:
        print(-1)
        sys.exit(0)
print(ans)