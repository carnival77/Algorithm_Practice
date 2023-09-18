import sys
input = sys.stdin.readline

n = 4
num = [[0] * n for _ in range(n)]
direction = [[0] * n for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        no = row[2 * j]
        d = row[2 * j + 1]
        d -= 1
        num[i][j] = no
        direction[i][j] = d

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def inBoard(nx, ny):
    if 0 <= nx < n and 0 <= ny < n:
        return True
    return False

# 물고기는 번호가 작은 물고기부터 순서대로 이동한다.
# 물고기는 한 칸을 이동할 수 있고,
# 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸,
# 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다.
# 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
# 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다.
# 그 외의 경우에는 그 칸으로 이동을 한다.
# 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.
def moveFish(num,direction,sx,sy):

    for no in range(1,n*n+1):
        find=False
        for x in range(n):
            for y in range(n):
                if num[x][y]==no:
                    find=True
                    d=direction[x][y]
                    for _ in range(8):
                        nx, ny = x + dx[d], y + dy[d]
                        if not inBoard(nx, ny) or (nx, ny) == (sx, sy):
                            d = (d + 1) % 8
                        else:
                            break
                    direction[x][y]=d
                    num[x][y],num[nx][ny]=num[nx][ny],num[x][y]
                    direction[x][y],direction[nx][ny]=direction[nx][ny],direction[x][y]
                if find: break
            if find: break
            
    return [num,direction]

def copyObject(a):
    return [row[:] for row in a]

def dfs(num,direction,x,y,d):

    # 물고기 이동
    num,direction=moveFish(num,direction,x,y)
    # 상어 이동
    # 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다.
    # 상어가 물고기가 있는 칸으로 이동했다면,
    # 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다.
    # 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다.
    # 물고기가 없는 칸으로는 이동할 수 없다.
    # 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다
    ans = 0
    for k in range(1,4):
        x,y=x+dx[d],y+dy[d]
        if not inBoard(x,y) or num[x][y]==0:
            continue
        nd=direction[x][y]
        no = num[x][y]
        num[x][y]=0
        direction[x][y]=0
        cur=no+dfs(copyObject(num),copyObject(direction),x,y,nd)
        num[x][y]=no
        direction[x][y]=nd
        ans=max(ans,cur)

    return ans

# 청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다.
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다
sx, sy = 0, 0
ans=num[sx][sy]
num[sx][sy]=0
sd=direction[sx][sy]
direction[sx][sy]=0
ans+=dfs(num,direction,sx,sy,sd) # 상어가 먹을 수 있는 물고기 번호의 합의 최댓값

print(ans)