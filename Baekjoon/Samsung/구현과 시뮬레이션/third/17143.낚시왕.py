import sys
input=sys.stdin.readline

n,m,l=map(int,input().split())
a=[[0]*m for _ in range(n)]
ans=0

class Shark:
    def __init__(self,s,d,z):
        self.s=s
        self.d=d
        self.z=z
        
#  상,하,우,좌
dx=[-1,1,0,0]
dy=[0,0,1,-1]

for _ in range(l):
    x,y,s,d,z=map(int,input().split())
    a[x-1][y-1]=Shark(s,d-1,z)
    
def get_reverse_direction(d):
    if d==0:
        return 1
    elif d==1:
        return 0
    elif d==2:
        return 3
    else:
        return 2
    
def get_next(x,y,dist,d):

    if d==0 or d==1: # 방향 = 상 or 하
        ny=y
        dist%=2*(n-1)
        if d==0: # 방향 = 상
            if dist<=x:
                nx=x-dist
            else:
                dist-=x
                if dist>0:
                    d=get_reverse_direction(d)
                if dist<=n-1:
                    nx=dist
                else:
                    dist-=n-1
                    if dist>0:
                        d=get_reverse_direction(d)
                    nx=n-1-dist
        else: # 방향 = 하
            if dist<=(n-1)-x:
                nx=x+dist
            else:
                dist-=(n-1)-x
                if dist>0:
                    d=get_reverse_direction(d)
                if dist<=n-1:
                    nx=n-1-dist
                else:
                    dist-=n-1
                    if dist>0:
                        d=get_reverse_direction(d)
                    nx=dist
    else: # 방향 = 좌 or 우
        nx=x
        dist%=2*(m-1)
        if d==3: # 방향 = 좌
            if dist<=y:
                ny=y-dist
            else:
                dist-=y
                if dist>0:
                    d=get_reverse_direction(d)
                if dist<=m-1:
                    ny=dist
                else:
                    dist-=m-1
                    if dist>0:
                        d=get_reverse_direction(d)
                    ny=m-1-dist
        else: # 방향 = 우
            if dist<=(m-1)-y:
                ny=y+dist
            else:
                dist-=(m-1)-y
                if dist>0:
                    d=get_reverse_direction(d)
                if dist<=m-1:
                    ny=m-1-dist
                else:
                    dist-=m-1
                    if dist>0:
                        d=get_reverse_direction(d)
                    ny=dist
    
    return [nx,ny,d]

def move():
    global a
    
    b=[[0]*m for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            if a[x][y]!=0:
                shark=a[x][y]
                s,d,z=shark.s,shark.d,shark.z
                nx,ny,nd=get_next(x,y,s,d)
                # print(nx,ny)
                if b[nx][ny]!=0 and b[nx][ny].z>z:
                    continue
                b[nx][ny]=Shark(s,nd,z)

    a=b

for y in range(m):
    for x in range(n):
        if a[x][y]!=0:
            ans+=a[x][y].z
            a[x][y]=0
            break
    move()

print(ans)