# solution 1. combinations 사용 - 시간 500ms 로 베스트
from itertools import combinations
from collections import deque

n,m = map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))

temp = [[0] * m for _ in range(n)]

def make_temp(n,m):
    for i in range(n):
        for j in range(m):
            temp[i][j] = board[i][j]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

zeros=[]
twos=[]

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            zeros.append((i,j))
        elif board[i][j] == 2:
            twos.append((i,j))

subs = combinations(zeros,3)

ans=0

def bfs(two):
    q = deque()
    x,y=two
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx,ny = x+dx[dir],y+dy[dir]
            if 0<=nx<n and 0<=ny<m:
                if temp[nx][ny] == 0:
                    temp[nx][ny]=2
                    q.append((nx,ny))

def safe(n,m):
    cnt=0
    for x in range(n):
        for y in range(m):
            if temp[x][y] == 0:
                cnt+=1
    return cnt

for sub in subs:
    make_temp(n,m)
    point1,point2,point3 = sub
    x1,y1,x2,y2,x3,y3=point1[0],point1[1],point2[0],point2[1],point3[0],point3[1]
    temp[x1][y1] = 1
    temp[x2][y2] = 1
    temp[x3][y3] = 1
    for two in twos:
        bfs(two)
    cnt = safe(n,m)
    ans=max(ans,cnt)

print(ans)


# solution 4. 백준 풀이. dfs.  서로 다른 3개의 요소를 n과 m내 영역에서 찾으려고 3중 for문을 사용. 비효율적으로 보인다.
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(b, x, y):
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
            b[nx][ny] = 2
            dfs(b, nx,ny)

def go():
    b = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]
    for i in range(n):
        for j in range(m):
            if b[i][j] == 2:
                dfs(b, i, j)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for x1 in range(n):
    for y1 in range(m):
        if a[x1][y1] != 0:
            continue
        for x2 in range(n):
            for y2 in range(m):
                if a[x2][y2] != 0:
                    continue
                for x3 in range(n):
                    for y3 in range(m):
                        if a[x3][y3] != 0:
                            continue
                        if x1 == x2 and y1 == y2:
                            continue
                        if x1 == x3 and y1 == y3:
                            continue
                        if x2 == x3 and y2 == y3:
                            continue
                        a[x1][y1] = 1
                        a[x2][y2] = 1
                        a[x3][y3] = 1
                        cur = go()
                        if ans < cur:
                            ans = cur
                        a[x1][y1] = 0
                        a[x2][y2] = 0
                        a[x3][y3] = 0
print(ans)


# solution 3. 백준 풀이. bfs. 서로 다른 3개의 요소를 n과 m내 영역에서 찾으려고 3중 for문을 사용. 비효율적으로 보인다.
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]
            if b[i][j] == 2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
                b[nx][ny] = 2
                q.append((nx,ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for x1 in range(n):
    for y1 in range(m):
        if a[x1][y1] != 0:
            continue
        for x2 in range(n):
            for y2 in range(m):
                if a[x2][y2] != 0:
                    continue
                for x3 in range(n):
                    for y3 in range(m):
                        if a[x3][y3] != 0:
                            continue
                        if x1 == x2 and y1 == y2:
                            continue
                        if x1 == x3 and y1 == y3:
                            continue
                        if x2 == x3 and y2 == y3:
                            continue
                        a[x1][y1] = 1
                        a[x2][y2] = 1
                        a[x3][y3] = 1
                        cur = bfs(a)
                        if ans < cur:
                            ans = cur
                        a[x1][y1] = 0
                        a[x2][y2] = 0
                        a[x3][y3] = 0
print(ans)


# # solution 2. 이코테 책 풀이. dfs를 활용한 벽 3개 설치. dfs 템플릿에 가장 적합. 1차원 배열이 아닌 2차원 배열을 dfs 로 조합을 구현한 것과, 바이러스를 퍼지게 하고, 안전 영역을 구하는 functions들을 각각 구현하여 알아보기 쉽게 구현한 것이 특징
from collections import deque
n,m = map(int,input().split())
board=[]
twos=[]
for i in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            twos.append((i,j))

temp = [[0] * m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

ans=0

def get_safe_zone():
    cnt=0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt+=1
    return cnt

def virus_def(x,y):

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx <= (n-1) and ny <= (m-1):
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus_def(nx,ny)

def dfs(count):
    global ans

    # 종료 조건
    if count == 3:
        # temp 배열 초기화
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]

        # 2인 칸들 bfs로 해서 바이러스 퍼뜨리기
        for two in twos:
            x,y=two
            # spread_virus_bfs(x,y)
            virus_def(x,y)

        # 안전 지역 넓이 최댓값 구하기
        cnt=get_safe_zone()
        ans=max(cnt,ans)
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                count+=1
                dfs(count)
                board[i][j]=0
                count-=1

dfs(0)

print(ans)

