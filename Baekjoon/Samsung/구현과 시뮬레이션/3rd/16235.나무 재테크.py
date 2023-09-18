import sys
input=sys.stdin.readline

n,m,l=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
b=[[5]*n for _ in range(n)]
t=[[[] for _ in range(n)] for _ in range(n)]
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

for _ in range(l):
    p=[[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            lived = []
            dead=0
            t[x][y].sort()
            for tree in t[x][y]:
                if b[x][y]>=tree:
                    b[x][y]-=tree
                    lived.append(tree+1)
                    if (tree+1) % 5 == 0:
                        for k in range(8):
                            nx, ny = x + dx[k], y + dy[k]
                            if not inBoard(nx, ny): continue
                            p[nx][ny]+=1
                else:
                    dead+=tree//2
            t[x][y]=lived
            b[x][y]+=dead
            b[x][y] += a[x][y]
    for x in range(n):
        for y in range(n):
            for _ in range(p[x][y]):
                t[x][y].append(1)

for i in range(n):
    for j in range(n):
        if len(t[i][j])>0:
            ans+=len(t[i][j])
print(ans)