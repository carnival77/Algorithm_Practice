import sys
from collections import deque
# from itertools import combinations

input=sys.stdin.readline

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
c=[[0]*n for _ in range(n)] # 디버깅용. 그룹 번호 맵
visit=[]
near=[]
groupCnt = []
groupNo = []
groupNums=[]
ans=[]
result=[]
count=0

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def bfs(sx,sy,num,no):
    global visit,c
    
    q=deque()
    q.append((sx,sy))
    visit[sx][sy]=True
    c[sx][sy]=no
    cnt=1
    
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if inBoard(nx,ny) and not visit[nx][ny] and a[nx][ny]==num:
                q.append((nx,ny))
                visit[nx][ny]=True
                c[nx][ny]=no
                cnt+=1
    
    return cnt

# def bfs2(sx, sy, gno):
#     global visit, near
#
#     q = deque()
#     q.append((sx, sy))
#     visit[sx][sy] = True
#
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]
#             if inBoard(nx, ny) and not visit[nx][ny] and c[nx][ny] == gno:
#                 q.append((nx, ny))
#                 visit[nx][ny] = True
#         for i in range(4):
#             nx1, ny1 = x + dx[i], y + dy[i]
#             if inBoard(nx1, ny1) and c[nx1][ny1] != gno:
#                 otherno = c[nx1][ny1]
#                 near[gno][otherno] += 1

def check():
    global visit,near, groupCnt,groupNo,groupNums,count

    groupCnt=[]
    groupNo=[]
    groupNums=[]
    
    # 그룹 정보 파악
    visit=[[False]*n for _ in range(n)]
    no=0
    for x in range(n):
        for y in range(n):
            if visit[x][y]: continue
            num=a[x][y]
            cnt=bfs(x,y,num,no)
            groupCnt.append(cnt)
            groupNo.append(no)
            groupNums.append(num)
            no+=1
    count=len(groupCnt)

    # 그룹 간 연결 관계 파악
    # visit = [[False] * n for _ in range(n)]
    # near=[[0]*count for _ in range(count)]
    # for x in range(n):
    #     for y in range(n):
    #         if visit[x][y]:continue
    #         gno = c[x][y]
    #         bfs2(x,y,gno)

    near=[[0]*count for _ in range(count)]
    for no in groupNo:
        for x in range(n):
            for y in range(n):
                if c[x][y]==no:
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if inBoard(nx,ny) and c[nx][ny]!=no:
                            x1=no
                            x2=c[nx][ny]
                            near[x1][x2]+=1

# def dfs(index,start,used,num,arr,n,m):
#     global result
#
#     if index==m:
#         result.append(arr[:])
#         return
#
#     for i in range(start,n):
#         if used[i]:
#             continue
#         used[i]=True
#         arr[index]=num[i]
#         dfs(index+1,i+1,used,num,arr,n,m)
#         used[i]=False

# def combinations(num,m):
#     global result
#
#     result=[]
#
#     l=len(num)
#     used=[False]*l
#     arr=[0]*m
#     dfs(0,0,used,num,arr,l,m)
#
#     return result

def getPoint():

    point=0
    
    # 그룹 및 그룹 간 연결 관계 파악
    check()
    
    # 점수 계산

    for a in range(count):
        for b in range(count):
            if a>b and near[a][b]>0:
                point += (groupCnt[a] + groupCnt[b]) * groupNums[a] * groupNums[b] * near[a][b]

    # for comb in combinations(groupNo,2):
    #     a,b=comb
    #     point+=(groupCnt[a]+groupCnt[b])*groupNums[a]*groupNums[b]*near[a][b]

    return point

def rotateClockWise(a):
    return list(map(list,zip(*a[::-1])))

def rotateCounterClockWise(a):
    return list(map(list, zip(*a)))[::-1]

def rotate():
    global a

    N=n//2
    # 십자 모양의 경우 통째로 반시계 방향으로 90' 회전
    b=[row[:] for row in a]
    b=rotateCounterClockWise(b)

    # 십자 모양을 제외한 4개의 정사각형은 각각 개별적으로 시계 방향으로 90'씩 회전
    for x in range(0,n,N+1):
        for y in range(0,n,N+1):
            part=[[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    part[i][j]=a[x+i][y+j]
            part=rotateClockWise(part)
            for i in range(N):
                for j in range(N):
                    b[x+i][y+j]=part[i][j]

    a=b

ans.append(getPoint())
for _ in range(3):
    rotate()
    ans.append(getPoint())

print(sum(ans))