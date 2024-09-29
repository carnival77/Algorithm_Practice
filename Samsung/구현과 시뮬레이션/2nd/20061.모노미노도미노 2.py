import sys
input=sys.stdin.readline

n=int(input())
g=[[0]*4 for _ in range(10)]
b=[[0]*10 for _ in range(4)]
ans=0
startInx=4
endInx=9

# 다음 칸에 블록이 이동 가능한 지
def check(nx,ny,kind):
    if kind==0:
        if nx>=endInx or g[nx+1][ny]!=0:
            return False
    else:
        if ny>=endInx or b[nx][ny+1]!=0:
            return False
    return True

# 블록 개별 이동.
# 블록을 놓을 위치를 빨간색 보드에서 선택하면, 그 위치부터 초록색 보드로 블록이 이동하고, 파란색 보드로 블록이 이동한다.
# 블록의 이동은 다른 블록을 만나거나 보드의 경계를 만나기 전까지 계속해서 이동한다.
def move(arr,kind):
    global g,b

    if kind==0:
        if len(arr)==1:
            sx,sy=arr[0]
            nx=sx+1
            ny=sy
            while check(nx,ny,0):
                nx+=1
            g[nx][ny]=1
        else:
            sx1,sy1=arr[0]
            sx2,sy2=arr[1]
            nx1=sx1+1
            ny1=sy1
            nx2=sx2+1
            ny2=sy2
            while check(nx1,ny1,0) and check(nx2,ny2,0):
                nx1+=1
                nx2+=1
            g[nx1][ny1]=1
            g[nx2][ny2]=1
    else:
        if len(arr)==1:
            sx,sy=arr[0]
            nx=sx
            ny=sy+1
            while check(nx,ny,1):
                ny+=1
            b[nx][ny]=1
        else:
            sx1,sy1=arr[0]
            sx2,sy2=arr[1]
            nx1=sx1
            ny1=sy1+1
            nx2=sx2
            ny2=sy2+1
            while check(nx1,ny1,1) and check(nx2,ny2,1):
                ny1+=1
                ny2+=1
            b[nx1][ny1]=1
            b[nx2][ny2]=1

def lay(arr):
    move(arr,0)
    move(arr,1)

# 초록색 보드에서 어떤 행이 타일로 가득 차 있다면, 그 행의 타일은 모두 사라진다.
# 사라진 이후에는 초록색 보드에서 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동한다.
# 파란색의 경우는 열이 타일로 가득 차 있으면, 그 열의 타일이 모두 사라지며, 사라진 이후에는 파란색 보드에서 사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동한다.
# 이렇게 한 행이나 열이 타일로 가득 차서 사라지면 1점을 획득한다. 점수는 사라진 행 또는 열의 수와 같다
def remove(t):
    global ans

    standardRow=0
    cnt=0

    for rowInx in range(startInx,endInx+1):
        row=t[rowInx]
        if row==[1]*4:
            cnt+=1
            standardRow=rowInx
            t[rowInx]=[0]*4

    if cnt>0:
        ans+=cnt
        for _ in range(cnt):
            for rowInx in range(standardRow,startInx,-1):
                t[rowInx],t[rowInx-1]=t[rowInx-1],t[rowInx]

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

for _ in range(n):
    t,x,y=map(int,input().split())

    # 블록 놓기
    if t==1:
        lay([[x,y]])
    elif t==2:
        lay([[x,y],[x,y+1]])
    else:
        lay([[x,y],[x+1,y]])

    # 행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 수 있다.
    # 이 경우에는 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후,
    # 연한 칸에 블록이 있는 경우를 처리해야 한다.
    # 블록 제거 및 블록 줄 이동, 점수 획득
    g=remove(g)
    b=transpose(remove(transpose(b)))

    # 연한 색 칸 블록 처리
    g=light(g)
    b=transpose(light(transpose(b)))

print(ans)
cnt=0
for x in range(endInx+1):
    for y in range(startInx):
        if g[x][y]==1:
            cnt+=1
        if b[y][x]==1:
            cnt+=1
print(cnt)