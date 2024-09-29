import sys
from collections import deque
input=sys.stdin.readline

n,m,=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] # 8 : 바다, 0 : 땅, 1 이상 : 섬 번호
for x in range(n):
    for y in range(m):
        if a[x][y]==0:
            a[x][y]=8
        elif a[x][y]==1:
            a[x][y]=0
ans=0

v=0 # 섬 개수
visited=[] # 섬별 그룹 짓기 과정에서 방문한 칸 표시
edges=[]
parent=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

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


def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def bfs(sx,sy,no):
    global a,visited

    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=True
    a[sx][sy]=no

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visited[nx][ny] and a[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=True
                a[nx][ny]=no

def makeGroup():
    global a,v,visited

    visited=[[False]*m for _ in range(n)]
    no=1
    for x in range(n):
        for y in range(m):
            if a[x][y]==0 and not visited[x][y]:
                bfs(x,y,no)
                no+=1
                v+=1

# 다리의 양 끝은 섬과 인접한 바다 위에 있어야 하고, 한 다리의 방향이 중간에 바뀌면 안된다.
# 또, 다리의 길이는 2 이상이어야 한다.
# 다리의 방향은 가로 또는 세로
# 다리가 교차하는 경우가 있을 수도 있다. 교차하는 다리의 길이를 계산할 때는 각 칸이 각 다리의 길이에 모두 포함되어야 한다
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
                break
            else:
                if a[nx][ny]==8:
                    q.append((nx,ny))
                    d[nx][ny]=d[x][y]+1
                elif a[nx][ny]==no:
                    break
                else:
                    if d[x][y] >= 2:
                        res.append([d[x][y],no,a[nx][ny]])

    return res

def makeBridge():
    global edges

    for x in range(n):
        for y in range(m):
            if a[x][y]==8: continue
            for edge in bfs2(x,y,a[x][y]):
                edges.append(edge)

def process():
    global ans,edges,parent

    makeBridge()

    parent = [0] * (v + 1)  # 부모 테이블 초기화
    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i
    edges.sort()

    for edge in edges:
        cost,x,y=edge
        x1=find_parent(parent, x)
        x2=find_parent(parent, y)
        if x1 != x2:
            union_parent(parent, x, y)
            ans += cost
            for i in range(2,v+1):
                if parent[i]==x2:
                    union_parent(parent,x1,i)

# 섬별 그룹 짓기
makeGroup()
# 섬 연결
process()
# 모든 섬을 연결하는 다리 길이의 최솟값
for i in range(2,v+1):
    if parent[i]!=1:
        print(-1)
        sys.exit(0)
print(ans)