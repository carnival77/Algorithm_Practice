import sys
input=sys.stdin.readline

n,m,l,g=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
c=[[0]*n for _ in range(n)]
ans=0

# 상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
# 대각선 4개 방향
dx2=[-1,1,-1,1]
dy2=[-1,1,1,-1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def grow():
    global a

    for x in range(n):
        for y in range(n):
            if -1<=a[x][y]<=0: continue
            cnt = 0
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if inBoard(nx, ny):
                    # 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장
                    if a[nx][ny] > 0:
                        cnt += 1
            a[x][y] += cnt

def spread():
    global a

    b = [row[:] for row in a]
    for x in range(n):
        for y in range(n):
            if -1 <= a[x][y] <= 0: continue
            cand = []
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if inBoard(nx, ny):
                    # 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행
                    if a[nx][ny] == 0 and c[nx][ny] == 0:
                        cand.append([nx, ny])
            # 이때 각 칸의 나무 그루 수에서 총 번식이 가능한 칸의 개수만큼 나누어진 그루 수만큼 번식이 되며,
            # 나눌 때 생기는 나머지는 버립니다. 번식의 과정은 모든 나무에서 동시에 일어나게 됩니다.
            if len(cand) > 0:
                plus = a[x][y] // len(cand)
                for i, j in cand:
                    b[i][j] += plus

    a=b

# 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
# 나무가 없는 칸에 제초제를 뿌리면 박멸되는 나무가 전혀 없는 상태로 끝이 나지만, 나무가 있는 칸에 제초제를 뿌리게 되면 4개의 대각선 방향으로 k칸만큼 전파되게 됩니다.
# 단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
# 제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라지게 됩니다.
# 제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지됩니다.
def kill():
    global a,c,ans

    # 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
    sx,sy = -1,-1
    max_kill=0
    cand=[]
    for x in range(n):
        for y in range(n):
            # 나무가 없는 칸(비어 있거나 벽)에 제초제를 뿌리면 박멸되는 나무가 전혀 없는 상태로 끝이 나지만,
            if -1<=a[x][y]<=0: continue
            # 나무가 있는 칸에 제초제를 뿌리게 되면 4개의 대각선 방향으로 k칸만큼 전파되게 됩니다.
            cnt=a[x][y]
            for k in range(4):
                for i in range(1,l+1):
                    nx, ny = x + dx2[k]*i, y + dy2[k]*i
                    if not inBoard(nx,ny): continue
                    # 단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
                    if -1<=a[nx][ny]<=0:
                        break
                    else:
                        cnt+=a[nx][ny]
            if cnt>=max_kill:
                max_kill=cnt
                cand.append([-max_kill,x,y])
    # 만약 박멸시키는 나무의 수가 동일한 칸이 있는 경우에는 행이 작은 순서대로, 만약 행이 같은 경우에는 열이 작은 칸에 제초제를 뿌리게 됩니다.
    if len(cand)>0:
        cand.sort()
        sx,sy=cand[0][1:]

    # 제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지됩니다.
    if (sx,sy)!=(-1,-1):
        x, y = sx, sy
        c[x][y] = g
        # 나무가 없는 칸에 제초제를 뿌리면 박멸되는 나무가 전혀 없는 상태로 끝이 나지만
        if a[x][y]==0:
            return
        ans += a[x][y]
        a[x][y] = 0
        for k in range(4):
            for i in range(1, l + 1):
                nx, ny = x + dx2[k] * i, y + dy2[k] * i
                if not inBoard(nx, ny): continue
                c[nx][ny] = g
                # 단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
                if -1 <= a[nx][ny] <= 0:
                    break
                else:
                    ans+=a[nx][ny]
                    a[nx][ny]=0

# 제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라지게 됩니다.
def decrease():
    global c

    for x in range(n):
        for y in range(n):
            if c[x][y]>0:
                c[x][y]-=1

def check():
    for x in range(n):
        for y in range(n):
            if a[x][y]>0:
                return True
    return False

for year in range(m):
    # 나무 존재 여부 판별
    check()
    # 성장
    grow()
    # 번식
    spread()
    # 제초제 제거
    if year>=1:
        decrease()
    # 제초제 뿌리기
    kill()

print(ans)