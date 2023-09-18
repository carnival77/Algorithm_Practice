import sys,heapq
input=sys.stdin.readline

MAX=2000

class Rabbit:
    def __init__(self,id,x,y,cnt):
        self.id=id
        self.x=x
        self.y=y
        self.cnt=cnt

    # 이동할 토끼를 결정하기 위해 정렬함수를 만들어줍니다.
    # 오름차순이 기본이며, 선행 원소가 후행 원소보다 '작아서', 음수가 나오면 두 원소의 위치를 바꾸지 않는다.
    # 선행 원소가 후행 원소보다 '커서', 양수가 나오면 두 원소의 위치를 바꾼다. 이를 통해 오름차순 정렬한다.
    def __lt__(self,other):
        if self.cnt!=other.cnt:
            return self.cnt<other.cnt
        if self.x+self.y!=other.x+other.y:
            return self.x+self.y<other.x+other.y
        if self.x != other.x :
            return self.x < other.x 
        if self.y!=other.y:
            return self.y<other.y
        return self.id<other.id
# 각 토끼의 id를 기록해줍니다.
pid=[0]*(MAX+1)
# 각 토끼의 현재 위치(좌표)를 기록해줍니다.
point=[[0,0]]*(MAX+1)
# 각 토끼의 이동거리를 기록해줍니다.
dist=[0]*(MAX+1)
# 각 토끼의 점수를 기록해줍니다.
score=[0]*(MAX+1)
# 각 토끼의 점프 횟수를 기록해줍니다.
jump_cnt=[0]*(MAX+1)
# 각각의 경주에서 토끼가 달렸는지 여부를 기록해줍니다.
jumped=[False]*(MAX+1)
# 하나를 제외한 모든 토끼의 점수를 더하는 쿼리를 편하게 하기 위해
# total_sum이라는 변수를 추가해줍니다.
total_sum=0
# 각 토끼의 id를 인덱스 번호로 변환해줍니다.
id_to_idx={}

def compare(self,other):
    if self.x + self.y != other.x + other.y:
        return self.x + self.y < other.x + other.y
    if self.x != other.x:
        return self.x < other.x
    if self.y != other.y:
        return self.y < other.y
    return self.id < other.id

# 상 = 주어진 방향
def go_up(x,y,d): # (x,y) : 위치 좌표, d : 남은 이동거리
    d%=2*(n-1) # 왕복하면 처음 위치로 돌아옴 -> 0 <= 남은 이동거리 <2*(n-1)
    if x-d>=1: # 이동 중 방향을 바꾸지 않고도 이동 가능한 거리라면, 이동
        x-=d # 이동한 곳으로 위치 변경
        d=0 # 남은 이동거리 = 0
    else: # 방향을 바꿔야 한다면, 주어진 방향의 가장 끝 지점으로 이동
        d-=(x-1) # 남은 이동거리는 이동한 만큼 낮추기
        x=1 # 위치는 주어진 방향 끝 지점
    if d>=n-x: # 여전히 이동 중 방향을 바꿔야 이동 가능한 거리라면(남은 이동거리가 가장 끝 점으로부터 반대편 끝까지 가기 위한 점프 횟수보다 높을 때),
        d-=(n-x) # 남은 이동 거리는 이동한 만큼 낮추고
        x=n # 반대 방향의 가장 끝 지점으로 이동.
    else: # 방향을 바꾸지 않아도 이동 가능한 거리라면
        x+=d # 이동한 곳으로 위치 변경
        d=0 # 남은 이동거리 = 0
    x-=d # 주어진 방향으로 남은 이동거리만큼 이동
    return [x,y]

# 하
def go_down(x,y,d):
    d%=2*(n-1)
    if x+d<=n:
        x+=d
        d=0
    else:
        d-=(n-x)
        x=n
    if d>=(x-1):
        d-=(x-1)
        x=1
    else:
        x-=d
        d=0
    x-=d
    return [x,y]

# 좌
def go_left(x,y,d):
    d%=2*(m-1)
    if y-d>=1:
        y-=d
        d=0
    else:
        d-=(y-1)
        y=1
    if d>=(m-y):
        d-=(m-y)
        y=m
    else:
        y+=d
        d=0
    y-=d
    return [x,y]

# 우
def go_right(x,y,d):
    d%=2*(m-1)
    if y+d<=m:
        y+=d
        d=0
    else:
        d-=(m-y)
        y=m
    if d>=y-1:
        d-=(y-1)
        y=1
    else:
        y-=d
        d=0
    y-=d
    return [x,y]

def copy_rabbit(rabbit):
    return Rabbit(rabbit.id,rabbit.x,rabbit.y,rabbit.cnt)

# 라운드 진행
def process(K,S):
    global total_sum

    pq=[]
    # 뛸 토끼 선정
    for i in range(p):
        x,y=point[i]
        id=pid[i]
        cnt=jump_cnt[i]
        heapq.heappush(pq,Rabbit(id,x,y,cnt))
        jumped[i]=False

    # 점프 진행
    for _ in range(1,K+1):
        cur_rabbit=heapq.heappop(pq)
        # 점프할 칸 선정
        id,x,y=cur_rabbit.id,cur_rabbit.x,cur_rabbit.y
        d=dist[id_to_idx[id]]
        # 해당 토끼를 상, 하, 좌, 우 4개의 방향으로 이동시킵니다.
        # 각각의 방향으로 이동시킨 후 최종 위치를 구하고
        # 가장 시작점으로부터 멀리 있는 위치를 찾아줍니다.
        nex_rabbit=copy_rabbit(cur_rabbit)
        nex_rabbit.x = 0
        nex_rabbit.y = 0
        # 상
        i, j = go_up(x, y, d)
        up_rabbit = copy_rabbit(cur_rabbit)
        up_rabbit.x,up_rabbit.y=i,j
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지를 갱신합니다.
        if compare(nex_rabbit,up_rabbit):
            nex_rabbit=up_rabbit
        # 하
        i, j = go_down(x, y, d)
        down_rabbit = copy_rabbit(cur_rabbit)
        down_rabbit.x,down_rabbit.y=i,j
        if compare(nex_rabbit,down_rabbit):
            nex_rabbit=down_rabbit
        # 좌
        i, j = go_left(x, y, d)
        left_rabbit = copy_rabbit(cur_rabbit)
        left_rabbit.x,left_rabbit.y=i,j
        if compare(nex_rabbit,left_rabbit):
            nex_rabbit=left_rabbit
        # 우
        i, j = go_right(x, y, d)
        right_rabbit = copy_rabbit(cur_rabbit)
        right_rabbit.x,right_rabbit.y=i,j
        if compare(nex_rabbit,right_rabbit):
            nex_rabbit=right_rabbit

        # 실제 point, jump_cnt 배열에도 값을 갱신해줍니다.
        nex_idx=id_to_idx[id]
        r,c=nex_rabbit.x,nex_rabbit.y
        point[nex_idx] = [r, c]
        jump_cnt[nex_idx]+=1
        # 토끼가 달렸는지 여부를 체크해줍니다.
        jumped[nex_idx]=True
        # 토끼의 점프 횟수를 갱신해주고, priority queue에 다시 집어넣습니다.
        nex_rabbit.cnt += 1
        heapq.heappush(pq,nex_rabbit)

        # 토끼가 받는 점수는 (현재 뛴 토끼)만 (r + c)만큼 점수를 빼주고,
        # 모든 토끼(total_sum)에게 (r + c)만큼 점수를 더해줍니다.
        # 최종적으로 i번 토끼가 받는 점수는 result[i] + total_sum이 됩니다.
        total_sum+=(r+c)
        score[nex_idx]-=(r+c)

    # 보너스 점수를 받을 토끼를 찾습니다.
    # 이번 경주때 달린 토끼 중 가장 멀리있는 토끼를 찾습니다.
    win_rabbit=Rabbit(0,0,0,0)
    while pq:
        cur_rabbit=heapq.heappop(pq)
        cur_idx=id_to_idx[cur_rabbit.id]

        if not jumped[cur_idx]:
            continue

        if compare(win_rabbit,cur_rabbit):
            win_rabbit=cur_rabbit
    # 해당 토끼에게 bonus만큼 점수를 추가해줍니다.
    win_inx=id_to_idx[win_rabbit.id]
    score[win_inx]+=S

# 이동거리를 변경합니다.
def changeDist(rid,L):
    rinx=id_to_idx[rid]
    dist[rinx]*=L

# 최고의 토끼를 선정합니다.
def present():
    ans=0
    for i in range(p):
        ans=max(ans,score[i]+total_sum)
    print(ans)

# 명령 입력 받기
Q=int(input())
for _ in range(Q):
    line=list(map(int,input().split()))
    cmd=line.pop(0)
    if cmd==100:
        n=line.pop(0)
        m=line.pop(0)
        p=line.pop(0)
        for i in range(p):
            id=line[2*i]
            d=line[2*i+1]
            pid[i]=id
            dist[i]=d
            id_to_idx[id]=i
            point[i]=[1,1]
    elif cmd==200:
        K,S=line[0],line[1]
        process(K,S)
    elif cmd==300:
        rid,L=line[0],line[1]
        changeDist(rid,L)
    else:
        present()
