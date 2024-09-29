import sys
from collections import deque
input=sys.stdin.readline

n,m,K=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
b=[[0]*n for _ in range(n)]

#  상,우,하,좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

units=dict() # 기사 딕셔너리
init_k=[0]*(m+1) # 초기 체력

for no in range(1,m+1):
    x,y,h,w,k=map(int,input().split())
    x-=1
    y-=1
    units[no]=[x,y,h,w,k]
    init_k[no]=k
    for i in range(x,x+h):
        for j in range(y,y+w):
            b[i][j]=no
# 왕에게 명령을 받은 기사는 상하좌우 중 하나로 한 칸 이동할 수 있습니다.
# 이때 만약 이동하려는 위치에 다른 기사가 있다면 그 기사도 함께 연쇄적으로 한 칸 밀려나게 됩니다.
# 그 옆에 또 기사가 있다면 연쇄적으로 한 칸씩 밀리게 됩니다.
# 하지만 만약 기사가 이동하려는 방향의 끝에 벽이 있다면 모든 기사는 이동할 수 없게 됩니다.
def try_movement(start,d):

    q=deque()
    q.append(start)
    move=set()
    move.add(start)
    dmg=[0]*(m+1)

    while q:
        now=q.popleft()
        x,y,h,w,k=units[now]
        nx,ny=x+dx[d],y+dy[d]

        # 기사가 이동하려는 방향의 끝에 벽이 있다면 모든 기사는 이동할 수 없게 됩니다
        # 범위 체크
        if not (nx>=0 and ny>=0 and nx+h-1<n and ny+w-1<n):return
        # 벽과 함정 체크
        for i in range(nx,nx+h):
            for j in range(ny,ny+w):
                if a[i][j]==2:
                    return
                # 각 기사들은 해당 기사가 이동한 곳에서 w×h 직사각형 내에 놓여 있는 함정의 수만큼만 피해를 입게 됩니다.
                if a[i][j]==1:
                    dmg[now]+=1
        # 연쇄적으로 다른 기사를 밀치는 지 체크하고, 밀치는 기사는 큐와 움직일 기사 후보에 삽입
        for other in units.keys():
            # 이미 움직인 기사 제외
            if other in move:continue

            ox,oy,oh,ow,ok=units[other]
            # 이번 기사의 이동 결과 다른 기사와 영역이 중복되는 지 아래 4가지 경우를 통해 체크한다.
            # 아래 4가지 경우는 4가지 방향으로 이동 시 영역이 중복되지 않는 경우의 수이다.
            # 4가지 경우 모두 True 여야 이동 시 겹치지 않는다.
            # 이번 기사가
            # 1) 아래로 이동 시, 위치를 옮긴 기사의 맨 아랫 칸(a)보다 다른 기사의 맨 윗 칸(b)이 더 아래
            #    즉, a이 b보다 더 작은 숫자로 더 위에 위치하는 지 체크
            # 2) 위로 이동 시, 위치를 옮긴 기사의 맨 윗 칸(a)보다 다른 기사의 맨 아랫 칸(b)이 더 위
            #    즉, a이 b보다 더 큰 숫자로 더 아래 위치하는 지 체크
            # 3) 오른쪽으로 이동 시, 위치를 옮긴 기사의 맨 오른쪽 칸(a)보다 다른 기사의 맨 왼쪽 칸(b)이 더 오른쪽
            #    즉, a이 b보다 더 작은 숫자로 더 왼쪽에 위치하는 지 체크
            # 4) 왼쪽으로 이동 시, 위치를 옮긴 기사의 맨 왼쪽 칸(a)보다 다른 기사의 맨 오른쪽 칸(b)이 더 왼쪽
            #    즉, a이 b보다 더 큰 숫자로 더 오른쪽에 위치하는 지 체크
            # 겹치지 않는 경우
            if nx+h-1<ox or ny+w-1<oy or nx>ox+oh-1 or ny>oy+ow-1:
                continue
            q.append(other)
            move.add(other)
    # 명령을 받은 기사는 피해를 입지 않으며
    dmg[start]=0
    # 움직일 기사 후보 내 기사들을 움직이고 정보 업데이트
    for no in move:
        x,y,h,w,k=units[no]
        # 각 기사마다 피해를 받은 만큼 체력이 깎이게 되며, 현재 체력 이상의 대미지를 받을 경우 기사는 체스판에서 사라지게 됩니다
        # 기사들은 모두 밀린 이후에 대미지를 입게 됩니다.
        if dmg[no]>=k:
            units.pop(no)
        else:
            nx,ny=x+dx[d],y+dy[d]
            units[no]=[nx,ny,h,w,k-dmg[no]]

    b = [[0] * n for _ in range(n)]
    for no in range(1,m+1):
        if no in units.keys():
            x,y,h,w,k=units[no]
            for i in range(x,x+h):
                for j in range(y,y+w):
                    b[i][j]=no

for round in range(1,K+1):
    no,d=map(int,input().split())
    # 체스판에서 사라진 기사에게 명령을 내리면 아무런 반응이 없게 됩니다.
    if no in units.keys():
        try_movement(no,d)

ans=0
for no in units:
    ans+=(init_k[no]-units[no][4])
print(ans)