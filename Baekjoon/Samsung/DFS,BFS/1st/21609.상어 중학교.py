import sys
from collections import deque
import heapq
input=sys.stdin.readline

n,m=map(int,input().split())
dx=[-1,0,1,0]
dy=[0,1,0,-1]

board=[list(map(int,input().split())) for _ in range(n)] # -1:검은색, 0:무지개, -2:빈 칸, 그 외:일반 컬러 블록
ans=0

# 블록 그룹 클래스
class Group:
    def __init__(self,color,normal,standard,gboard=None,cnt=0,rainbow=0):
        self.color=color # 블록 색
        self.cnt=cnt # 그룹 내 블록 개수
        self.rainbow=rainbow # 그룹 내 무지개 블록 개수
        self.normal=normal # 그룹 내 일반 블록 개수
        self.standard=standard # 기준 블록
        self.gboard=gboard # 블록 그룹 상태맵

# 격자 내 판단
def inBoard(nx,ny):
    return 0<=nx<n and 0<=ny<n

# 주어진 위치 기준 탐색하여 그룹 짓기
def bfs(sx,sy,visit):
    global board

    q=deque()
    q.append([sx,sy])
    visit[sx][sy]=True
    color=board[sx][sy]
    # 해당 블록 그룹의 상태맵
    gboard=[[-1]*n for _ in range(n)]
    gboard[sx][sy]=color
    group=Group(color,1,[sx,sy]) # 해당 블록의 색, 일반 블록 개수 1, 기준 블록 위치 설정하여 그룹 객체 생성

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny):
                #
                if not visit[nx][ny] and (board[nx][ny]==color or board[nx][ny]==0):
                    visit[nx][ny]=True
                    q.append([nx,ny])
                    gboard[nx][ny]=color
                    if board[nx][ny]==color:
                        group.normal+=1
                        # 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
                        group.standard=min(group.standard,[nx,ny])
                    elif board[nx][ny]==0:
                        group.rainbow+=1
    group.cnt=group.normal+group.rainbow
    group.gboard=gboard
    # 그룹에는 일반 블록이 적어도 하나 있어야 하며, 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며,
    if group.cnt>=2 and group.normal>=1:
        return [group,visit]
    else:
        return [None,visit]

# 블록 그룹 짓기
# 블록 그룹은 연결된 블록의 집합이다.
# 그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다.
# 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다.
# 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며,
# 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다.
# 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
def makeGroup():
    global board

    groups=[]
    # 컬러별 탐색
    for color in range(1,m+1):
        # 컬러별 방문 블록 맵을 설정한다. 이를 통해, 위치가 다르고 컬러가 같은 블록이 격자 내 무지개 블록을 활용하여 각각 그룹을 형성할 수 있도록 한다.
        visit=[[False] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                # 해당 컬러이며, 아직 bfs로 탐색하지 않았다면 탐색
                if board[x][y]==color and not visit[x][y]:
                    # 그룹 객체와 컬러별 방문 블록 맵을 받는다.
                    group,visit=bfs(x,y,visit)
                    if group is not None:
                        groups.append(group)
    return groups

# 해당 블록 그룹 빈 칸 처리
# 해당 블록 그룹의 상태맵으로 격자에서 해당 그룹에 속한 블록을 빈 칸 처리
def deleteGroup(gboard):
    global board

    for x in range(n):
        for y in range(n):
            if gboard[x][y]!=-1:
                board[x][y]=-2

# 중력 작용
# 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다. 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.
def gravity():
    global board

    cnt=1
    while cnt:
        cnt=0
        for x in range(n-1):
            for y in range(n):
                if board[x][y]>=0 and board[x+1][y]==-2:
                    board[x+1][y],board[x][y]=board[x][y],board[x+1][y]
                    cnt+=1

# 반시계 90도 회전
# 격자가 90도 반시계 방향으로 회전
def rotateCounterClockwise(a):
    return list(map(list,zip(*a)))[::-1]

while True:
    #블록 그룹 짓기
    groups=makeGroup()
    if len(groups)==0:
        print(ans)
        break

    # 가장 큰 블록 그룹 제거, 포인트 획득
    arr=[]
    # 크기가 가장 큰 블록 그룹을 찾는다.
    # 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹,
    # 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을,
    # 그 것도 여러개이면 열이 가장 큰 것을 찾는다
    for group in groups:
        arr.append([-group.cnt,-group.rainbow,-group.standard[0],-group.standard[1],group.gboard])
    heapq.heapify(arr)
    first=heapq.heappop(arr)
    # 포인트 획득
    ans+=(first[0])**2
    # 해당 블록 그룹 빈 칸 처리
    deleteGroup(first[-1])

    # 중력 작용
    gravity()

    # 90도 반시계 회전
    board=rotateCounterClockwise(board)

    # 중력 작용
    gravity()