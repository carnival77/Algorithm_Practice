import sys
input=sys.stdin.readline
MAX=101

def generate(dirs):
    tmp=dirs[:]
    for i in range(len(dirs)-1,-1,-1):
        tmp.append((dirs[i]+1)%4)

    dirs=tmp

    return dirs

n=int(input())
c=[[0]*MAX for _ in range(MAX)]
ans=0

#  우,상,좌,하
dx=[0,-1,0,1]
dy=[1,0,-1,0]

def process(x,y,d,g):
    global c

    dirs=[d]
    for _ in range(g):
        dirs=generate(dirs)

    c[x][y]=1
    for k in dirs:
        nx,ny=x+dx[k],y+dy[k]
        c[nx][ny]=1
        x,y=nx,ny

for _ in range(n):
    y,x,d,g=map(int,input().split())
    process(x,y,d,g)

for x in range(MAX-1):
    for y in range(MAX-1):
        if c[x][y]==c[x+1][y]==c[x+1][y+1]==c[x][y+1]==1:
            ans+=1
print(ans)