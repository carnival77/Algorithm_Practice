from collections import deque

n,K=map(int,input().split())
a=list(map(int,input().split())) # 어항 배열
b=[] # 어항 데크 배열
ans=0

dx=[-1,0,1,0]
dy=[0,-1,0,1]

# 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다.
# 만약, 그러한 어항이 여러개라면 물고기의 수가 최소인 어항 모두에 한 마리씩 넣는다
def insert():
    global a

    min_v=min(a)
    for i in range(len(a)):
        if a[i]==min_v:
            a[i]+=1

# 먼저, 가장 왼쪽에 있는 어항을 그 어항의 오른쪽에 있는 어항의 위에 올려 놓아
# 2개 이상 쌓여있는 어항을 모두 공중 부양시킨 다음, 전체를 시계방향으로 90도 회전시킨다.
# 이후 공중 부양시킨 어항을 바닥에 있는 어항의 위에 올려놓는다.
# 바닥의 가장 왼쪽에 있는 어항 위에 공중 부양시킨 어항 중 가장 왼쪽에 있는 어항이 있어야 한다.
# 이 작업은 공중 부양시킨 어항 중 가장 오른쪽에 있는 어항의 아래에 바닥에 있는 어항이 있을때까지 반복한다.
def stack():
    global b

    c=[]
    for _ in range(n):
        q=deque()
        c.append(q)

    for v in a:
        c[0].append(v)
    c[1].append(c[0].popleft())

    while True:
        d = []
        for _ in range(n):
            q = deque()
            d.append(q)
        tmp = []
        start_inx=-1
        for i in range(len(c[0])-1,-1,-1):
            q = deque()
            j = 1
            try:
                while c[j][i] is not None:
                    q.append(c[j][i])
                    j+=1
            except:
                pass
            if len(q) >= 1:
                q.appendleft(c[0][i])
                if start_inx == -1:
                    start_inx = i
                tmp.append(q)
        i=1
        for q in tmp:
            d[i]=q
            i+=1
        q=deque()
        for i in range(start_inx+1,len(c[0])):
            q.append(c[0][i])
        d[0]=q

        if len(d[1])<=len(d[0]):
            c=d
        else:
            break

    b=c

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

# 어항에 있는 물고기의 수를 조절
# 모든 인접한 두 어항에 대해서, 물고기 수의 차이를 구한다.
# 이 차이를 5로 나눈 몫을 d라고 하자.
# d가 0보다 크면, 두 어항 중 물고기의 수가 많은 곳에 있는 물고기 d 마리를 적은 곳에 있는 곳으로 보낸다.
# 이 과정은 모든 인접한 칸에 대해서 동시에 발생한다.
def control():
    global b

    tmp=[[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for k in range(4):
                nx,ny=x+dx[k],y+dy[k]
                if not inBoard(nx,ny):continue
                try:
                    if b[x][y]>b[nx][ny]:
                        d=(b[x][y]-b[nx][ny])//5
                        if d>0:
                            tmp[x][y]-=d
                            tmp[nx][ny]+=d
                except:
                    pass
    for x in range(n):
        for y in range(n):
            if tmp[x][y]==0:continue
            b[x][y]+=tmp[x][y]

# 어항을 바닥에 일렬로 놓아야 한다.
# 가장 왼쪽에 있는 어항부터, 그리고 아래에 있는 어항부터 가장 위에 있는 어항까지 순서대로 바닥에 놓아야 한다
def sorting():
    global a

    c=[]
    for y in range(n):
        for x in range(n):
            try:
                c.append(b[x][y])
            except:
                pass

    a=c

#  가운데를 중심으로 왼쪽 N/2개를 공중 부양시켜 전체를 시계 방향으로 180도 회전 시킨 다음, 오른쪽 N/2개의 위에 놓아야 한다.
#  이 작업은 두 번 반복해야한다.
#  두 번 반복하면 바닥에 있는 어항의 수는 N/4개가 된다
def stack2():
    global b

    c = []
    for _ in range(n):
        q = deque()
        c.append(q)
    c[0]=deque(a)

    level=1
    for i in range(1,3):
        N=n//(2*i)
        inx=2*i-1
        tmp=[]
        for j in range(level):
            q=deque()
            for k in range(N):
                q.appendleft(c[j][k])
            tmp.append(q)
        for q in tmp:
            c[inx]=q
            inx-=1
        tmp=[]
        for j in range(level):
            q=deque()
            for k in range(N):
                q.append(c[j][N+k])
            tmp.append(q)
        for inx2,q in enumerate(tmp):
            c[inx2]=q
        level+=1

    b=c

def check():
    if max(a)-min(a)<=K:
        return True
    return False

while True:
    ans += 1
    # 물고기 넣기
    insert()
    # 어항 쌓기
    stack()
    # 물고기 수 조절
    control()
    # 어항 정렬
    sorting()
    # 어항 쌓기 - 2
    stack2()
    # 물고기 수 조절
    control()
    # 어항 정렬
    sorting()

    if check():
        break

print(ans)