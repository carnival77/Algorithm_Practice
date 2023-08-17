import sys,heapq
input=sys.stdin.readline

class Rabbit:
    def __init__(self,id,cnt,x,y):
        self.id=id
        self.cnt=cnt
        self.x=x
        self.y=y

    # 우선순위는 순서대로 (현재까지의 총 점프 횟수가 적은 토끼, 현재 서있는 행 번호 + 열 번호가 작은 토끼,
    # 행 번호가 작은 토끼, 열 번호가 작은 토끼, 고유번호가 작은 토끼) 순
    def __lt__(self, other):
        if self.cnt!=other.cnt:
            return self.cnt<other.cnt
        if self.x+self.y!=other.x+other.y:
            return self.x+self.y<other.x+other.y
        if self.x!=other.x:
            return self.x<other.x
        if self.y!=other.y:
            return self.y<other.y
        if self.id!=other.id:
            return self.id<other.id

# # (행 번호 + 열 번호가 큰 칸, 행 번호가 큰 칸, 열 번호가 큰 칸) 순
def compare(self,other):
    if self.x + self.y != other.x + other.y:
        return self.x + self.y < other.x + other.y
    if self.x != other.x:
        return self.x < other.x
    if self.y != other.y:
        return self.y < other.y
    if self.id != other.id:
        return self.id < other.id

MAX=2000
q=int(input())
points=[[0,0]]*(MAX+1)
pid=[0]*(MAX+1)
dist=[0]*(MAX+1)
score=[0]*(MAX+1)
jump_cnt=[0]*(MAX+1)
jump=[False]*(MAX+1)
id_to_inx=dict()
total_sum=0

def get_reverse_direction(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2

def get_next(x, y, dist, d):
    if d == 0 or d == 1:  # 방향 = 상 or 하
        ny = y
        dist %= 2 * (n - 1)
        if d == 0:  # 방향 = 상
            if dist <= x:
                nx = x - dist
            else:
                dist -= x
                if dist > 0:
                    d = get_reverse_direction(d)
                if dist <= n - 1:
                    nx = dist
                else:
                    dist -= n - 1
                    if dist > 0:
                        d = get_reverse_direction(d)
                    nx = n - 1 - dist
        else:  # 방향 = 하
            if dist <= (n - 1) - x:
                nx = x + dist
            else:
                dist -= (n - 1) - x
                if dist > 0:
                    d = get_reverse_direction(d)
                if dist <= n - 1:
                    nx = n - 1 - dist
                else:
                    dist -= n - 1
                    if dist > 0:
                        d = get_reverse_direction(d)
                    nx = dist
    else:  # 방향 = 좌 or 우
        nx = x
        dist %= 2 * (m - 1)
        if d == 3:  # 방향 = 좌
            if dist <= y:
                ny = y - dist
            else:
                dist -= y
                if dist > 0:
                    d = get_reverse_direction(d)
                if dist <= m - 1:
                    ny = dist
                else:
                    dist -= m - 1
                    if dist > 0:
                        d = get_reverse_direction(d)
                    ny = m - 1 - dist
        else:  # 방향 = 우
            if dist <= (m - 1) - y:
                ny = y + dist
            else:
                dist -= (m - 1) - y
                if dist > 0:
                    d = get_reverse_direction(d)
                if dist <= m - 1:
                    ny = m - 1 - dist
                else:
                    dist -= m - 1
                    if dist > 0:
                        d = get_reverse_direction(d)
                    ny = dist

    return [nx, ny]

def copy_rabbit(rabbit):
    return Rabbit(rabbit.id,rabbit.cnt,rabbit.x,rabbit.y)

# 가장 우선순위가 높은 토끼를 뽑아 멀리 보내주는 것을 K번 반복합니다.
def process(k,s):
    global total_sum

    # 토끼 우선순위 큐 생성 및 데이터 삽입
    pq=[]
    for i in range(p):
        id=pid[i]
        cnt=jump_cnt[i]
        x,y=points[i]
        heapq.heappush(pq,Rabbit(id,cnt,x,y))
        jump[i]=False

    # 점프 진행
    for turn in range(1,k+1):
        cur_rabbit=heapq.heappop(pq)
        # 우선순위가 가장 높은 토끼가 결정이 되면 이 토끼를 i번 토끼라 했을 때
        # 상하좌우 네 방향으로 각각 di만큼 이동했을 때의 위치를 구합니다.
        # 이때 이동하는 도중 그 다음 칸이 격자를 벗어나게 된다면 방향을 반대로 바꿔 한 칸 이동하게 됩니다.
        # 이렇게 구해진 4개의 위치 중 (행 번호 + 열 번호가 큰 칸, 행 번호가 큰 칸, 열 번호가 큰 칸) 순으로 우선순위를 두었을 때
        # 가장 우선순위가 높은 칸을 골라 그 위치로 해당 토끼를 이동
        # 이 과정에서 동일한 토끼가 여러번 선택되는 것 역시 가능
        id=cur_rabbit.id
        x=cur_rabbit.x
        y=cur_rabbit.y
        d=dist[id_to_inx[id]]
        next_rabbit=copy_rabbit(cur_rabbit)
        # (행 번호 + 열 번호가 큰 칸, 행 번호가 큰 칸, 열 번호가 큰 칸) 순
        # 4가지 방향 : 상,하,우,좌
        cand=[]
        for k in range(4):
            nx,ny=get_next(x,y,d,k)
            cand.append([nx+ny,nx,ny])
        cand.sort(key=lambda x:(-x[0],-x[1],-x[2]))
        nx,ny = cand[0][-2:]
        next_rabbit.x, next_rabbit.y =nx,ny

        next_inx=id_to_inx[id]
        jump_cnt[next_inx] += 1
        points[next_inx]=[next_rabbit.x,next_rabbit.y]
        jump[next_inx]=True

        next_rabbit.cnt += 1
        heapq.heappush(pq,next_rabbit)

        # 이 칸의 위치를 (ri,ci)라 했을 때 i번 토끼를 제외한 나머지 P−1마리의 토끼들은
        # 전부 ri+ci만큼의 점수를 동시에 얻게 됩니다.
        r, c = next_rabbit.x + 1, next_rabbit.y + 1
        total_sum+=r+c
        score[next_inx]-=r+c

    # 라운드 승자 선택
    # (현재 서있는 행 번호 + 열 번호가 큰 토끼, 행 번호가 큰 토끼, 열 번호가 큰 토끼, 고유번호가 큰 토끼) 순으로
    # 우선순위를 두었을 때 가장 우선순위가 높은 토끼를 골라 점수 S를 더해주게 됩니다.
    # 단, 이 경우에는 K번의 턴 동안 한번이라도 뽑혔던 적이 있던 토끼 중
    # 가장 우선순위가 높은 토끼를 골라야만 함에 꼭 유의
    win_rabbit=Rabbit(0,0,0,0)
    while pq:
        cur_rabbit=heapq.heappop(pq)
        cur_inx=id_to_inx[cur_rabbit.id]
        if not jump[cur_inx]: continue
        if compare(win_rabbit,cur_rabbit):
            win_rabbit=cur_rabbit
    win_inx=id_to_inx[win_rabbit.id]
    score[win_inx]+=s

# 고유번호가 pidt인 토끼의 이동거리를 L배 해줍니다.
# 단, 계산 도중 특정 토끼의 이동거리가 10억을 넘어가는 일은 발생하지 않음을 가정해도 좋습니다.
def change(id,l):

    dist[id_to_inx[id]]*=l

def selectFinalWinner():

    maxVal=0
    for i in range(p):
        if score[i]+total_sum>maxVal:
            maxVal=score[i]+total_sum

    print(maxVal)
    sys.exit(0)

for _ in range(q):
    line=list(map(int,input().split()))
    cmd=line.pop(0)
    # (1) 경주 시작 준비
    if cmd==100:
        n=line.pop(0)
        m=line.pop(0)
        p=line.pop(0)
        for i in range(p):
            id, d = line[2*i:2*i + 2]
            pid[i]=id
            dist[i]=d
            id_to_inx[id]=i
    # (2) 경주 진행
    elif cmd==200:
        k,s=line
        process(k,s)
    # (3) 이동거리 변경
    elif cmd==300:
        id,l=line
        change(id,l)
    # (4) 최고의 토끼 선정
    else:
        selectFinalWinner()