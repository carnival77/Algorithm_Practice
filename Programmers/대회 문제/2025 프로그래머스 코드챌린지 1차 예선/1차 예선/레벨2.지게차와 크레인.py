from collections import deque

n,m=0,0
dx=[-1,0,1,0]
dy=[0,-1,0,1]
a=[]
visit=[]
cand=[]

def copyBoard(a):
    return [row[:] for row in a]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<m:
        return True
    return False

def bfs(a,sx,sy,tg):
    global visit,cand

    q=deque()
    start=(sx,sy)
    q.append(start)
    visit[sx][sy]=True

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visit[nx][ny]:
                if a[nx][ny]=="0":
                    q.append((nx,ny))
                    visit[nx][ny]=True
                if a[nx][ny]==tg:
                    visit[nx][ny]=True
                    cand.append((nx,ny))

def process_one(tg):
    global a,visit,cand

    visit = [[False] * m for _ in range(n)]
    cand=[]

    tmp=copyBoard(a)
    for x in range(n):
        for y in range(m):
            if x==0 or x==n-1 or y==0 or y==m-1:
                if visit[x][y]:continue
                if a[x][y]==tg:
                    cand.append((x,y))
                if a[x][y]=="0":
                    bfs(tmp,x,y,tg)

    for x,y in cand:
        tmp[x][y]="0"
    a=tmp

def process_two(tg):
    global a

    for x in range(n):
        for y in range(m):
            if a[x][y]==tg:
                a[x][y]="0"

def solution(storage, requests):
    global n,m,a,visit
    ans=0

    for row in storage:
        a.append(list(row))

    n=len(a)
    m=len(a[0])

    for request in requests:
        tg=request[0]
        if len(request)==1:
            process_one(tg)
        if len(request)==2:
            process_two(tg)

    for x in range(n):
        for y in range(m):
            if a[x][y]!="0":
                ans+=1

    # for row in a:
    #     print(row)

    return ans

# storage=["AZWQY", "CAABX", "BBDDA", "ACACA"]
storage=["HAH", "HBH", "HHH", "HAH", "HBH"]
# requests=["A", "BB", "A"]
requests=["C", "B", "B", "B", "B", "H"]
print(solution(storage,requests))