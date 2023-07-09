import sys
input=sys.stdin.readline

class FireBall:
    def __init__(self,m,s,d):
        self.m=m
        self.s = s
        self.d=d

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

ans=0

n,m,k=map(int,input().split())
a=[[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r,c,m,s,d=map(int,input().split())
    a[r-1][c-1].append(FireBall(m,s,d))

def move():
    global a

    b=[[[] for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if len(a[x][y])>0:
                for fb in a[x][y]:
                    d,s=fb.d,fb.s
                    nx=(x+dx[d]*s)%n
                    ny=(y+dy[d]*s)%n
                    b[nx][ny].append(fb)
                a[x][y].clear()
    a=b

def process(x,y):

    # 2.1. 합치기(같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다)
    tm,ts,cnt,even,odd,ok,res=0,0,len(a[x][y]),0,0,False,[]
    for fb in a[x][y]:
        tm+=fb.m
        ts+=fb.s
        # 파이어볼은 4개의 파이어볼로 나누어진다.
        # 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다
        # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다
        if fb.d%2==0:
            even+=1
        else:
            odd+=1
    # 질량이 0인 파이어볼은 소멸되어 없어진다.
    if tm>=5:
        # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋
        m=tm//5
        # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
        s=int(ts/cnt)
        if even==0 or odd==0:
            ok=True
        if ok:
            for d in range(0,8,2):
                res.append(FireBall(m,s,d))
        else:
            for d in range(1,8,2):
                res.append(FireBall(m,s,d))
    return res

for _ in range(k):
    # 1. 파이어볼 이동(모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동)
    move()
    # 2. 이동 후, 2개 이상 있는 칸에서
    for x in range(n):
        for y in range(n):
            if len(a[x][y])>=2:
                a[x][y]=process(x,y)

for x in range(n):
    for y in range(n):
        for fb in a[x][y]:
            ans+=fb.m
print(ans)
