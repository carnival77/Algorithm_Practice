import sys
input=sys.stdin.readline

MAX=sys.maxsize
n=10
m=5
a=[list(map(int,input().split())) for _ in range(n)]
cnt=[-1]+[5]*5

# 1을 모두 덮는 것이 불가능한 경우
def possible(a):
    for x in range(n):
        for y in range(n):
            if a[x][y]==1:
                return False
    return True

def inBoard(nx,ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    return False

def check(a,k,x,y):

    for i in range(k):
        for j in range(k):
            nx=x+i
            ny=y+j
            if not inBoard(nx,ny) or a[nx][ny]==0:
                return False
    return True

def attach(a,k,x,y):

    for i in range(k):
        for j in range(k):
            nx=x+i
            ny=y+j
            a[nx][ny]=0

    return a

def detach(a,k,x,y):

    for i in range(k):
        for j in range(k):
            nx=x+i
            ny=y+j
            a[nx][ny]=1

    return a

# 색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류가 있으며,
# 각 종류의 색종이는 5개씩 가지고 있다.
# 색종이를 크기가 10×10인 종이 위에 붙이려고 한다.
# 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 0 또는 1이 적혀 있다.
# 1이 적힌 칸은 모두 색종이로 덮여져야 한다.
# 색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다.
# 또, 칸의 경계와 일치하게 붙여야 한다. 0이 적힌 칸에는 색종이가 있으면 안 된다.
def dfs(a,z,num,cnt):

    if z==n*n:
        ok=possible(a)
        # -1을 출력
        if not ok:
            return -1
        # 모든 1을 덮는데 성공한 경우이면, 필요한 색종이의 최소 개수 반환
        else:
            return num

    x=z//n
    y=z%n
    res=MAX

    if a[x][y]==1:
        for k in range(m,0,-1):
            if cnt[k]<=0: continue
            ok=check(a,k,x,y)
            if ok:
                a = attach(a, k, x, y)
                cnt[k]-=1
                tmp=dfs(a,z+1,num+1,cnt)
                cnt[k]+=1
                detach(a,k,x,y)
                res=min(res,tmp)
    else:
        tmp = dfs(a, z + 1, num,cnt)
        res = min(res, tmp)

    return res

# 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수
ans=dfs(a,0,0,cnt)

if ans==MAX:
    ans=-1
print(ans)