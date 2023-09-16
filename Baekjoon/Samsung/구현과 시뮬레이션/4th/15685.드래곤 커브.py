import sys
input=sys.stdin.readline

MAX=101

#  우,상,좌,하
dx=[0,-1,0,1]
dy=[1,0,-1,0]

n=int(input())
a=[[0]*MAX for _ in range(MAX)]
ans=0

def generate(a):

    for d in a[::-1]:
        x=(d+1)%4
        a.append(x)

    return a

def inBoard(nx,ny):
    if 0<=nx<MAX and 0<=ny<MAX:
        return True
    return False

for _ in range(n):
    y,x,d,g=map(int,input().split())
    a[x][y]=1
    gen=[d]
    for _ in range(g):
        gen=generate(gen)
    for z in gen:
        x+=dx[z]
        y+=dy[z]
        a[x][y]=1

for x in range(MAX):
    for y in range(MAX):
        if inBoard(x+1,y) and inBoard(x,y+1) and inBoard(x+1,y+1) and a[x][y]==a[x+1][y]==a[x][y+1]==a[x+1][y+1]==1:
            ans+=1

print(ans)