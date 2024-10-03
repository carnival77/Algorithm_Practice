# 1차 풀이 : 실패
# 2차 풀이 : 성공(약 1시간 소요)

# import sys
# sys.stdin = open("input.txt", "r")

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def connect(a,sx,sy,d):

    route=[]
    x,y=sx,sy
    xdir=dx[d]
    ydir=dy[d]

    # 주어진 방향으로 탐색하여, 벽까지 연결 가능한지 확인
    ok=False
    while True:
        nx,ny=x+xdir,y+ydir
        if inBoard(nx,ny):
            if a[nx][ny]!=0:
                break
            else:
                route.append([nx,ny])
        else:
            ok=True
            break
        x,y=nx,ny

    # 연결 가능하면 연결 루트와 거리 반환
    if ok:
        dist=len(route)
        return [route,dist]
    else:
        return [None,-1]

def dfs(a,inx,cnt,length):
    global cand

    # 마지막 코어까지 다 연결 시도 완료했다면
    if inx==core_cnt:
        # 현재까지의 연결 코어 개수, 길이 저장
        cand.append([cnt,length])
        return

    sx,sy=cores[inx]
    for d in range(4): # 4방향으로
        route,dist=connect(a,sx,sy,d) # 연결 시도
        if route is not None: # 연결 가능하면
            for x,y in route: # 전선 설치
                a[x][y]=2
            # 코어 개수와 전선 길이 합산하고 전선 설치된 맵에서 다음 코어부터의 연결 시도
            dfs(a,inx+1,cnt+1,length+dist)
            for x,y in route: # 전선 제거
                a[x][y]=0
    # 4방향 다 연결 시도했으면 다음 코어로 순서 넘기기
    dfs(a,inx+1,cnt,length)

T = int(input())
for t in range(1, T + 1):
    n=int(input())
    a=[list(map(int,input().split())) for _ in range(n)]
    cores=[] # 미완성 core 위치
    cand=[] # 각 경우의 수에서의 완성 코어 개수/길이 배열

    for x in range(1,n-1):
        for y in range(1,n-1):
            if a[x][y]==1:
                cores.append([x,y])

    core_cnt=len(cores)
    dfs(a,0,0,0) # 코어 0번부터 n-1번까지 연결 시도

    cand.sort(key=lambda x:(-x[0],x[1])) # 코어 개수순 내림차순, 전선 길이 순 오름차순 정렬
    tot_cnt,ans=cand[0]

    print("#"+str(t),ans)