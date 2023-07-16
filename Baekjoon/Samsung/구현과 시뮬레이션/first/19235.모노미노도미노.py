import sys
input=sys.stdin.readline

n=int(input())
g=[[0]*4 for _ in range(10)]
b=[[0]*10 for _ in range(4)]
ans=0
startInx=4
endInx=9

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def inBoard(nx,ny):
    if 0<=nx<endInx+1 and 0<=ny<startInx:
        return True
    return False

# 다음 칸에 블록이 이동 가능한 지
def check(nx,ny,t):
    if nx>endInx or ny>endInx or t[nx][ny]!=0:
        return False
    return True

# 블록 개별 이동.
# 블록을 놓을 위치를 빨간색 보드에서 선택하면, 그 위치부터 초록색 보드로 블록이 이동하고, 파란색 보드로 블록이 이동한다.
# 블록의 이동은 다른 블록을 만나거나 보드의 경계를 만나기 전까지 계속해서 이동한다.
def move(arr,no,t):
    if len(arr)==1:
        sx,sy=arr[0]
        nx=sx
        ny=sy
        while check(nx+1,ny,t):
            nx+=1
        t[nx][ny]=no
    else:
        sx1,sy1=arr[0]
        sx2,sy2=arr[1]
        nx1=sx1
        ny1=sy1
        nx2=sx2
        ny2=sy2
        # 가로 블록
        if abs(ny1-ny2)==1:
            while check(nx1+1,ny1,t) and check(nx2+1,ny2,t):
                nx1+=1
                nx2+=1
        # 세로 블록
        elif abs(nx1 - nx2) == 1:
            while check(nx2+1,ny2,t):
                nx1+=1
                nx2+=1
        t[nx1][ny1]=no
        t[nx2][ny2]=no

    return t

# 초록색 보드에서 어떤 행이 타일로 가득 차 있다면, 그 행의 타일은 모두 사라진다.
# 사라진 이후에는 초록색 보드에서 각 블록이 다른 블록을 만나거나 경계를 만나기 전까지 아래로 이동한다.
# 이 때 주의할 점은, (1) 블록 단위로 이동하는 것, (2) 가득 찬 행/열이 여러 개가 동시에 생긴다면, 모두 없애고 블록을 이동시켜야 한다.
# 파란색의 경우는 열이 타일로 가득 차 있으면, 그 열의 타일이 모두 사라지며,
# 사라진 이후에는 파란색 보드에서 각 블록이 다른 블록을 만나거나 경계를 만나기 전까지 오른쪽으로 이동한다.
# 이렇게 한 행이나 열이 타일로 가득 차서 사라지면 1점을 획득한다. 점수는 사라진 행 또는 열의 수와 같다
def remove(t,arr):
    global ans

    cnt=len(arr)
    standardRow=arr[0]

    for rowInx in range(standardRow,standardRow+cnt):
        t[rowInx]=[0]*4

    ans+=cnt
    done=set()
    for x in range(standardRow-1,startInx-1,-1):
        for y in range(4):
            if t[x][y]>=1 and t[x][y] not in done:
                size=1
                no=t[x][y]
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if inBoard(nx,ny) and t[nx][ny]==no:
                        size+=1
                        x2,y2=nx,ny
                if size==1:
                    tmp=[row[:] for row in t]
                    tmp[x][y]=0
                    t=move([[x,y]],no,tmp)
                elif size>=2:
                    tmp=[row[:] for row in t]
                    tmp[x][y]=0
                    tmp[x2][y2]=0
                    t=move([[x2,y2],[x,y]],no,tmp)
                done.add(no)

    return t

def transpose(t):
    return list(map(list,zip(*t)))

# 초록색 보드의 0, 1번 행에 블록이 있으면, 블록이 있는 행의 수만큼 아래 행에 있는 타일이 사라지고,
# 초록색 보드의 모든 블록이 사라진 행의 수만큼 아래로 이동하고,
# 파란색 보드의 0, 1번 열에 블록이 있으면,
# 블록이 있는 열의 수만큼 오른쪽 열에 있는 타일이 사라지고, 파란색 보드의 모든 블록이 사라진 열의 수만큼 이동하게 된다
def light(t):
    cnt=0
    for rowInx in range(startInx,6):
        if t[rowInx]!=[0]*4:
            t[endInx-cnt]=[0]*4
            cnt+=1
    if cnt>0:
        for _ in range(cnt):
            for rowInx in range(endInx,startInx,-1):
                t[rowInx],t[rowInx-1]=t[rowInx-1],t[rowInx]

    return t

# 가득 찬 행의 인덱스 반환
def check2(t):
    arr=[]
    for x in range(startInx,endInx+1):
        res=True
        for y in range(4):
            if t[x][y]==0:
                res=False
                break
        if res:
            arr.append(x)
    return arr

no=1 # 블록 번호.
for _ in range(n):
    t,x,y=map(int,input().split())

    # 블록 놓기
    if t==1:
        g=move([[x,y]],no,g)
        b=transpose(move([[y,x]],no,transpose(b)))
    elif t==2:
        g=move([[x,y],[x,y+1]],no,g)
        b=transpose(move([[y,x],[y+1,x]],no,transpose(b)))
    else:
        g = move([[x,y],[x+1,y]], no,g)
        b = transpose(move([[y, x], [y, x+1]], no,transpose(b)))

    no+=1

    # 행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 수 있다.
    # 이 경우에는 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후,
    # 연한 칸에 블록이 있는 경우를 처리해야 한다.
    # 블록의 이동 때문에, 다시 행이나 열이 타일로 가득차는 경우가 또 발생할 수도 있다.
    # 이 경우에도 1점을 얻고, 그 행이나 열의 모든 타일을 제거하고 다시 나머지 블록을 이동하면 된다.
    # 블록 제거 및 블록 줄 이동, 점수 획득
    while True:
        res=check2(g)
        if res:
            g = remove(g,res)
        else:
            break
    while True:
        res=check2(transpose(b))
        if res:
            b=transpose(remove(transpose(b),res))
        else:
            break

    # 연한 색 칸 블록 처리
    g=light(g)
    b=transpose(light(transpose(b)))

print(ans)
cnt=0
for x in range(endInx+1):
    for y in range(startInx):
        if g[x][y]>=1:
            cnt+=1
        if b[y][x]>=1:
            cnt+=1
print(cnt)