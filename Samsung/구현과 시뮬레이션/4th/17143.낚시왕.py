import sys
input=sys.stdin.readline

class Shark:
    def __init__(self,no,x,y,s,d,size):
        self.no=no
        self.x=x
        self.y=y
        self.s=s
        self.d=d
        self.size=size
        
#  상,하,우,좌
dx=[-1,1,0,0]
dy=[0,0,1,-1]

n,m,l=map(int,input().split())
a=[[0]*m for _ in range(n)]
ans=0
sharks=[]

def getNext(x,y,s,d):
    
    if 0<=d<=1:
        s%=2*(n-1)
        if d==0:
            if s<=x:
                x-=s
            else:
                s-=x
                x=0
                d=1
                if s<=n-1:
                    x+=s
                else:
                    s-=n-1
                    x=n-1
                    d=0
                    x-=s
            return [x,y,d]
        else:
            if s<=n-1-x:
                x+=s
            else:
                s-=n-1-x
                x=n-1
                d=0
                if s<=n-1:
                    x-=s
                else:
                    s-=n-1
                    x=0
                    d=1
                    x+=s
            return [x,y,d]

    elif 2<=d<=3:
        s%=2*(m-1)
        if d==3:
            if s<=y:
                y-=s
            else:
                s-=y
                y=0
                d=2
                if s<=m-1:
                    y+=s
                else:
                    s-=m-1
                    y=m-1
                    d=3
                    y-=s
            return [x,y,d]
        else:
            if s<=m-1-y:
                y+=s
            else:
                s-=m-1-y
                y=m-1
                d=3
                if s<=m-1:
                    y-=s
                else:
                    s-=m-1
                    y=0
                    d=2
                    y+=s
            return [x,y,d]

def move():
    global a,sharks
    
    b=[[0]*m for _ in range(n)]
    
    for shark in sharks:
        if shark==None: continue
        no,x,y,s,d,size=shark.no,shark.x,shark.y,shark.s,shark.d,shark.size
        nx,ny,nd=getNext(x,y,s,d)
        shark.x,shark.y,shark.d=nx,ny,nd
        if b[nx][ny]==0:
            b[nx][ny]=shark
        else:
            other=b[nx][ny]
            if other.size<shark.size:
                b[nx][ny]=shark
                sharks[other.no]=None
            elif other.size>shark.size:
                sharks[no]=None
    a=b

for no in range(l):
    r,c,s,d,size=map(int,input().split())
    r-=1
    c-=1
    d-=1
    shark=Shark(no,r,c,s,d,size)
    a[r][c]=shark
    sharks.append(shark)

for y in range(m):
    for x in range(n):
        if a[x][y]!=0:
            ans+=a[x][y].size
            sharks[a[x][y].no] = None
            a[x][y]=0
            break
    move()

print(ans)