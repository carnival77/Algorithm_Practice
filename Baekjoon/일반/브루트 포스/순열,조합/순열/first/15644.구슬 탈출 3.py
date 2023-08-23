import sys
from itertools import product

input=sys.stdin.readline
MAX=int(1e9)

n,m=map(int,input().split())
a=[list(input()) for _ in range(n)]

#  우,하,좌,상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

rx,ry,bx,by=0,0,0,0

for x in range(1,n-1):
    for y in range(1,m-1):
        if a[x][y]=='R':
            rx,ry=x,y
        elif a[x][y]=='B':
            bx,by=x,y

# 연이어 같은 방향이나 반대 방향이 나오는 경우는 제외
def valid(arr):
    for i in range(9):
        if arr[i] == arr[i + 1]:
            return False
        if arr[i]%2 == arr[i+1]%2:
            return False
    return True

# 4개 방향(상,하,좌,우) 중 10개를 중복 허용, 순서 상관하여 뽑는 중복 순열의 모든 경우의 수를 탐색한다.
def generate():
    cand=[] # 모든 경우의 수의 개수는 4 X 2^9
    for prod in product([0,1,2,3],repeat=10):
        if valid(prod):
            cand.append(prod)
    return cand

def inBoard(nx,ny):
    if 0<nx<n-1 and 0<ny<m-1:
        return True
    return False

# 구슬 이동 루트 확인. 이때, 구슬이 더 이상 이동할 수 없을 때까지 이동시킨다.
def go(rx,ry,bx,by,d):

    # O에 도달했는지
    r_res=False
    b_res=False
    R,B=[r_res,[rx,ry]],[b_res,[bx,by]]
    ok1,ok2=True,True # 각 구슬이 더 움직일 필요가 있는지

    while ok1 or ok2:
        # 빨간 구슬 이동
        while ok1:
            nx, ny = rx + dx[d], ry + dy[d]
            # 다음 칸이 벽이거나 범위 밖이면 중지.
            if a[nx][ny]=='#' or not inBoard(nx,ny):
                ok1=False
                break
            # 다음 칸이 다른 구슬이고
            elif (nx,ny)==(bx,by):
                # 그 다음 칸이 벽이 아닐 경우
                if a[nx+dx[d]][ny+dy[d]]!='#':
                    # 다른 구슬을 이동시킨 후 다시 이동
                    ok1=True
                    break
                # 그 다음 칸이 벽일 경우 중지
                else:
                    ok1=False
                    break
            # 다음 칸이 O이면 True 반환
            elif a[nx][ny]=='O':
                r_res=True
                rx,ry=0,0
                ok1 = False
                break
            else: # 그 외의 경우는 다음 칸으로 이동
                rx,ry=nx,ny
        R = [r_res, [rx, ry]]

        # 파란 구슬 이동
        while ok2:
            nx, ny = bx + dx[d], by + dy[d]
            # 다음 칸이 벽이거나 범위 밖이면 중지.
            if a[nx][ny]=='#' or not inBoard(nx,ny):
                ok2 = False
                break
            # 다음 칸이 다른 구슬이고
            elif (nx,ny)==(rx,ry):
                # 그 다음 칸이 벽이 아닐 경우
                if a[nx+dx[d]][ny+dy[d]]!='#':
                    # 다른 구슬을 이동시킨 후 다시 이동
                    ok2=True
                    break
                # 그 다음 칸이 벽일 경우 중지
                else:
                    ok2=False
                    break
            # 다음 칸이 O이면 True 반환
            elif a[nx][ny]=='O':
                b_res=True
                bx,by=0,0
                ok2 = False
                break
            else:  # 그 외의 경우는 다음 칸으로 이동
                bx,by=nx,ny
        B = [b_res, [bx, by]]

    return [R,B]

# 방향 조합대로 맵 기울이기
def move(dirs,rx,ry,bx,by):

    cnt=0
    # 각 중복순열의 방향대로 R,B를 맵에서 이동시킨다.
    for d in dirs: # 이번 방향으로 기울일 때
        cnt+=1
        R,B=go(rx,ry,bx,by,d) # 구슬 이동 루트 확인
        # 실패 : 파란 구슬이 구멍에 빠지는 경우
        if B[0]:
            break
        # 성공 : R만 O에 빠지고 B는 O에 안 빠지는 경우, 횟수 반환
        if R[0] and not B[0]:
            return cnt
        rx,ry=R[1]
        bx,by=B[1]

    return MAX

def process():

    ans=MAX
    ans2=[]
    tmp=[]
    cand=generate()
    for dirs in cand:
        # ans=min(ans,move(dirs,rx,ry,bx,by))
        res=move(dirs,rx,ry,bx,by)
        if ans>res:
            ans=res
            tmp=dirs[:ans]
    if ans!=MAX:
        for dir in tmp:
            #  우,하,좌,상
            if dir==0:
                ans2.append('R')
            elif dir==1:
                ans2.append('D')
            elif dir==2:
                ans2.append('L')
            else:
                ans2.append('U')

    return [ans,ans2]

ans,ans2=process()
if ans==MAX:
    print(-1)
else:
    print(ans)
for a in ans2:
    print(a,end='')