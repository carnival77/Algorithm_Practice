import sys
from collections import deque
input=sys.stdin.readline

n=int(input()) # board의 변의 길이
m=0 # 그룹의 개수
ans=0 # 총합

dx=[-1,0,1,0]
dy=[0,1,0,-1]
board=[list(map(int,input().split())) for _ in range(n)]
group_board=[[-1]*n for _ in range(n)] # 그룹 맵

class Group:
    def __init__(self,no,num,cnt=0):
        self.no=no # 그룹 번호
        self.num=num # 숫자
        self.cnt=cnt # 칸의 수

groups=[] # 그룹 객체 배열
near_cnt=[] # 이웃한 그룹 간 변의 수

# 격자 내부 판단
def in_board(nx,ny):
    global n
    return (0<=nx<n and 0<=ny<n)

# bfs 탐색 - 그룹 짓기
def bfs(visit,num,x,y):
    global groups,board,group_board,n

    q=deque()
    q.append([x,y])
    group=Group(len(groups),num)
    group.cnt+=1
    group_board[x][y]=group.no
    visit[x][y]=True
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if in_board(nx,ny):
                if not visit[nx][ny] and board[nx][ny]==num:
                    visit[nx][ny]=True
                    q.append([nx,ny])
                    group.cnt+=1
                    group_board[nx][ny]=group.no
    groups.append(group)

    return visit

# 동일한 숫자가 상하좌우로 인접해있는 경우 동일한 그룹
def makeGroup():
    global group_board,near_cnt,n,m

    visit=[[False]*n for _ in range(n)]
    # 그룹별 숫자, 칸의 수 설정
    for x in range(n):
        for y in range(n):
            if visit[x][y]: continue
            visit=bfs(visit,board[x][y],x,y)

    m=len(groups)
    near_cnt = [[0]*m for _ in range(m)] # 이웃한 그룹 간 변의 수

    # 이웃한 그룹 간 변의 수 설정
    for x in range(n):
        for y in range(n):
            for k in range(4):
                nx,ny=x+dx[k],y+dy[k]
                if in_board(nx, ny) and group_board[nx][ny] > group_board[x][y]:
                    a=group_board[x][y]
                    b=group_board[nx][ny]
                    near_cnt[a][b]+=1

# 예술 점수는 모든 그룹 쌍의 조화로움의 합으로 정의됩니다. 그룹 a와 그룹 b의 조화로움은 (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수로 정의
# 그룹 쌍 간의 조화로움 값이 0보다 큰 조합의 조화로움 값을 전부 더하기
def calculateBeauty():
    global ans,near_cnt,groups,m

    for x in range(m):
        for y in range(m):
            if near_cnt[x][y]>0:
                a=groups[x]
                b=groups[y]
                ans+=(a.cnt+b.cnt)*a.num*b.num*near_cnt[x][y]

# 시계방향 90도 회전
def rotateClockwise(a):
    return list(map(list,zip(*a[::-1])))

# 반시계방향 90도 회전
def rotateCounterClockwise(a):
    return list(map(list,zip(*a)))[::-1]

# 십자 모양의 경우 통째로 반시계 방향으로 90' 회전
def rotateCenter():
    global board,n

    center=n//2
    b=rotateCounterClockwise(board)
    for y in range(n):
        board[center][y]=b[center][y]
    for x in range(n):
        board[x][center]=b[x][center]

# 십자 모양을 제외한 4개의 정사각형은 각각 개별적으로 시계 방향으로 90'씩 회전
def rotateSide():
    global board,n

    center=n//2
    b1=[[0]*center for _ in range(center)]
    b2=[[0]*center for _ in range(center)]
    b3=[[0]*center for _ in range(center)]
    b4=[[0]*center for _ in range(center)]
    for x in range(center):
        for y in range(center):
            b1[x][y]=board[x][y]
            b2[x][y]=board[x][y+center+1]
            b3[x][y]=board[x+center+1][y]
            b4[x][y]=board[x+center+1][y+center+1]
    b1=rotateClockwise(b1)
    b2=rotateClockwise(b2)
    b3=rotateClockwise(b3)
    b4=rotateClockwise(b4)
    for x in range(center):
        for y in range(center):
            board[x][y]=b1[x][y]
            board[x][y+center+1]=b2[x][y]
            board[x+center+1][y]=b3[x][y]
            board[x+center+1][y+center+1]=b4[x][y]

# 초기 예술 점수
# 그룹 만들기
makeGroup()
# 예술성 계산
calculateBeauty()
for _ in range(3):
    #  중앙 십자 회전
    rotateCenter()
    # 모서리 4개 정사각형 회전
    rotateSide()
    # 그룹 만들기
    makeGroup()
    # 예술성 계산
    calculateBeauty()

print(ans)