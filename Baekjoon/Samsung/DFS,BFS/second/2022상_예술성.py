import sys
from itertools import combinations
from collections import deque
input=sys.stdin.readline

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
g=[[-1]*n for _ in range(n)]
ans=[0]*4
groupCnt=0
groupInfo=[]
m=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def rotateCounterClockwise(a):
    return list(map(list,zip(*a)))[::-1]

def rotateClockwise(a):
    return list(map(list,zip(*a[::-1])))

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def bfs1(sx,sy,num,no):
    global g

    q=deque()
    q.append((sx,sy))
    visited=[[False]*n for _ in range(n)]
    visited[sx][sy]=True
    g[sx][sy]=no
    cnt=1

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and a[nx][ny]==num and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=True
                g[nx][ny]=no
                cnt+=1

    return cnt

def makeGroup():
    global g,groupCnt,groupInfo

    g = [[-1] * n for _ in range(n)]
    no=0
    groupInfo=[]
    for x in range(n):
        for y in range(n):
            if g[x][y]==-1:
                cnt=bfs1(x,y,a[x][y],no)
                no+=1
                groupInfo.append([cnt,a[x][y]])
    groupCnt=no

# 그룹 a와 그룹 b의 조화로움은 (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
def getPoint(step):
    global ans,m,a
    
    m=[[0]*(groupCnt) for _ in range(groupCnt)]

    for no in range(groupCnt):
        for x in range(n):
            for y in range(n):
                if g[x][y]==no:
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if inBoard(nx,ny) and g[nx][ny]!=no:
                            x1=no
                            x2=g[nx][ny]
                            m[x1][x2]+=1
    
    point=0
    for x1 in range(groupCnt):
        for x2 in range(groupCnt):
            if x1>x2 and m[x1][x2]>0:
                a_cnt,a_num=groupInfo[x1]
                b_cnt,b_num=groupInfo[x2]
                point+=(a_cnt+b_cnt)*a_num*b_num*m[x1][x2]
    ans[step]=point

def rotate():
    global a

    b=[row[:] for row in a]

    # 십자 모양의 경우 통째로 반시계 방향으로 90' 회전
    b=rotateCounterClockwise(b)
    # 십자 모양을 제외한 4개의 정사각형은 각각 개별적으로 시계 방향으로 90'씩 회전이 진행
    N=n//2
    for x in range(0,n,N+1):
        for y in range(0,n,N+1):
            part = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    part[i][j]=a[x+i][y+j]
            part=rotateClockwise(part)
            for i in range(N):
                for j in range(N):
                    b[x+i][y+j]=part[i][j]

    a=b

for step in range(4):
    # 그룹 짓기
    makeGroup()
    # 점수 구하기
    getPoint(step)
    # 회전
    rotate()

print(sum(ans))