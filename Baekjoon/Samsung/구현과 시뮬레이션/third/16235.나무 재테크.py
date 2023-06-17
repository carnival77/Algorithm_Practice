import sys
input=sys.stdin.readline

n,m,l=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
b=[[5]*n for _ in range(n)]
t=[[[] for _ in range(n)] for _ in range(n)]
d=[]
ans=0

dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

for _ in range(m):
    x,y,z=map(int,input().split())
    x-=1
    y-=1
    t[x][y].append(z)

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False
    
def spring():
    global b,t,d
    
    d=[[[] for _ in range(n)] for _ in range(n)]
    tmp=[[[] for _ in range(n)] for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if len(t[x][y])>0:
                t[x][y].sort()
                for i in range(len(t[x][y])):
                    if b[x][y]>=t[x][y][i]:
                        b[x][y]-=t[x][y][i]
                        t[x][y][i]+=1
                        tmp[x][y].append(t[x][y][i])
                    else:
                        d[x][y].append(t[x][y][i])

    t=tmp

def summer():
    global b
    
    for x in range(n):
        for y in range(n):
            if len(d[x][y])>0:
                for dead in d[x][y]:
                    b[x][y]+=dead//2

def fall():
    global t

    for x in range(n):
        for y in range(n):
            if len(t[x][y]) > 0:
                for tree in t[x][y]:
                    if tree%5==0:
                        for k in range(8):
                            nx,ny=x+dx[k],y+dy[k]
                            if not inBoard(nx,ny):continue
                            t[nx][ny].append(1)

def winter():
    global b

    for x in range(n):
        for y in range(n):
            b[x][y]+=a[x][y]

for _ in range(l):
    #봄
    spring()
    #여름
    summer()
    #가을
    fall()
    #겨울
    winter()

for i in range(n):
    for j in range(n):
        if len(t[i][j])>0:
            ans+=len(t[i][j])
print(ans)