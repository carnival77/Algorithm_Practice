nums=list(map(int,input().split()))
r=b=None # 말판 정보 딕셔너리
blue_start=[5,10,15] # 이동을 시작하는 파란색 칸의 인덱스
score=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,22,24,28,27,26,25,30,35,0] # 칸 인덱스별 점수
end=32
ans=0

products=[] # 4개의 말을 10번을 중복하여 순서 상관하여 뽑는 모든 경우의 수

def dfs(index,nums,arr,used,n,m):
    global products

    if index==m:
        products.append(arr[:])
        return

    for i in range(n):
        used[i]=True
        arr[index]=nums[i]
        dfs(index+1,nums,arr,used,n,m)
        used[i]=False

def product(nums,m):
    n=len(nums)
    used=[False]*n
    arr=[0]*m
    dfs(0,nums,arr,used,n,m)

def init():
    global r,b

    # 말을 고르는 모든 경우의 수 구하기
    product([0,1,2,3],10)

    # 말판 정보 딕셔너리에 삽입. 도착 칸은 32
    r=dict()
    b=dict()

    for i in range(20):
        r[i] = i + 1
    r[20] = end

    b[5] = 21
    b[21] = 22
    b[22] = 23
    b[23] = 29
    b[10] = 24
    b[24] = 25
    b[25] = 29
    b[15] = 26
    b[26] = 27
    b[27] = 28
    b[28] = 29
    b[29] = 30
    b[30] = 31
    b[31] = 20
    b[20] = end

# 말은 게임판에 그려진 화살표의 방향대로만 이동할 수 있다.
# 말이 파란색 칸에서 이동을 시작하면 파란색 화살표를 타야 하고, 이동하는 도중이거나 파란색이 아닌 칸에서 이동을 시작하면 빨간색 화살표를 타야 한다.
# 말이 도착 칸으로 이동하면 주사위에 나온 수와 관계 없이 이동을 마친다.
def getNext(p,num):
    global routes

    now = pos[p]
    if now in blue_start:
        routes[p] = 'b'
    route = routes[p]
    if route=='r':
        route = r
    else:
        route = b

    for i in range(num):
        if now == end:
            break
        now=route[now]

    return now

# 초기 설정
init()

for prod in products:
    res=0
    pos=[0]*4
    done = [False] * 4  # 말 도착 여부
    routes = ['r'] * 4  # 초기 말 루트
    ok=True # 이번 순열으로 모든 주사위 값대로 말들이 이동하는가. 이동하지 못하는 말이 있는 순열은 제외.
    # 도착 칸에 있지 않은 말을 하나 골라 주사위에 나온 수만큼 이동시킨다.
    for p,num in zip(prod,nums):
        if done[p]:
            ok=False
            break
        # 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다.
        # 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.
        next_pos=getNext(p,num)
        if next_pos in pos and next_pos!=end:
            ok=False
            break
        # 말 이동
        pos[p]=next_pos
        # 말이 도착 칸으로 이동하면 주사위에 나온 수와 관계 없이 이동을 마친다.
        if next_pos==end:
            done[p]=True
        else:
            # 말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가된다.
            res+=score[next_pos]
    if ok:
        ans=max(ans,res)

print(ans)