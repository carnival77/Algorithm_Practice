재귀 문제 풀 때, 탐색 최대 범위 설정. 파이썬의 기본 재귀 깊이 제한은 1000 밖에 안 된다.
sys.setrecursionlimit(10**6)
10**6 정도가 적당히 큰 수이다.
이것과 함께 dfs 를 사용할 때는 pypy3 가 아닌 python을 사용 언어로 설정하자

# 조합 문제. N개 중 M개를 선택하여 중복 허용 X, 순서 상관하며 사용. 즉, 순서가 달라도 같은 요소로 구성되어 있으면 같은 집합
from itertools import combinations

for i in combinations(arr, m):
# 순열 문제. N개 중 M개를 선택하여 중복 허용 X, 순서 상관 없이 사용. 즉, 순서가 다르고 같은 요소로 구성되어 있으면 다른 집합
from itertools import permutations

for i in permutations(arr, m):
# 중복 순열 문제. N개 중 M개를 선택하여 중복 허용 O, 순서 상관 없이 사용. 즉, 순서가 다르고 같은 요소로 구성되어 있으면 다른 집합
from itertools import product

for i in product(arr,repeat=m):
# 중복조합 : N개의 수 중 M개를 순서 상관하여 중복 허용하여 뽑는다.
from itertools import combinations_with_replacement

for i in combinations_with_replacement(arr,m):

1. board = [list(input()) for _ in range(n)]
: 정수 배열을 행렬로 입력
CCP
CCP
PPC

[['C', 'C', 'P'], ['C', 'C', 'P'], ['P', 'P', 'C']]

% 주의! input = sys.stdin.readline 으로 설정하면, 엔터(/n)도 같이 입력되니 주의
ex ) [['C', 'C', 'P', '\n'], ['C', 'C', 'P', '\n'], ['P', 'P', 'C', '\n']]

# 리스트 슬라이싱
1. a[N:M] N부터 M 전까지
a[N] <= x < a[M]
a[N] <= x <= a[M-1]
N을 포함한 인덱스 부터 M을 포함하지 않는 인덱스 까지를 자르는 기능을 합니다.
특이사항! M이 실제 리스트의 크기를 넘어서는 수이면, 인덱스 오류가 발생하는 것이 아니라, 자동으로 리스트의 맨 마지막 요소까지로 인식한다.

2. a[:M] M 전까지
a[0] <= x < a[M]
a[0] <= x <= a[M-1]

3. a[N:] N 부터
a[N] <= x < a[len(a)]
a[N] <= x <= a[len(a) - 1]
len(a)는 리스트의 길이를 말합니다.

4. a[:] 이처럼 양쪽을 비워서 슬라이싱을 한다는 것은 리스트 전체를 복사하는것과 동일합니다.
a[0] <= x < a[len(a)]
a[0] <= x <= a[len(a) - 1]

# reverse
temp = temp[::-1]

# 복사(copy)
# 1차원 리스트의 깊은복사
a = [i for i in range(10000000)]
b = a[:]

# 2차원 리스트의 깊은복사
a = [[i for i in range(1000)] for _ in range(1000)]
b = [row[:] for row in a]

# 2차원 배열 시계/반시계 방향 회전
# 시계 방향 회전
temp = a[i][7]
for j in range(7, 0, -1):
    a[i][j] = a[i][j - 1]
a[i][0] = temp

# 반시계 방향 회전
temp = a[i][0]
for j in range(7):
    a[i][j] = a[i][j + 1]
a[i][7] = temp

# 우측(시계 방향)으로 k번 rotate
a = a[-k:] + a[:-k]
# 좌측(반시계 방향)으로 rotate
c = c[k:] + c[:k]

>>> a = ['a', 'b', 'c', 'd', 'e']
>>> a[  : -1 ]
['a', 'b', 'c', 'd']

# 줄바꿈 없이 출력
print("안녕하세요", end=' ')

- ''.join(리스트)
''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수인 것입니다.

- '구분자'.join(리스트)
'구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.
'_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.

#직사각형 매트릭스 조작
# 배열 시계방향 90도 회전
def rotated(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[i][j] = a[n-1-j][i]
  return result

list(map(list, zip(*a[::-1])))

# 배열 반시계방향 90도 회전 = 시계방향 90도로 3번 회전
def op4(a):
    n = len(a)
    b = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            b[i][j] = a[j][n-1-i]

    return b

list(map(list, zip(*a)))[::-1]

n, m = 4, 6
arr = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]

# 매트릭스 상하 반전
arr = arr[::-1]

def op1(a):
    n=len(a)
    b=[[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            b[i][j] = a[n-1-i][j]

    return b

# 매트릭스 좌우 반전
for i in range(n):
    arr[i] = arr[i][::-1]

def op2(a):
    n=len(a)
    b=[[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            b[i][j] = a[i][n-j-1]

    return b

# 매트릭스 행렬 변환
list(map(list, zip(*a)))

# 부분 매트릭스를 한 칸으로 생각하고 매트릭스 전체 상하반전.
def op5(a):
    global size
    # 부분 칸 개수
    sub_cnt = size//sub_size
    ans = list([0] * size for _ in range(size))

    for i in range(sub_cnt):
        for j in range(sub_cnt):
            # 기존 상하반전 식의 b[i][j] = a[n-1-i][j] 과 같이 적용하여, 칸 간의 상하반전
            x1=i*sub_size
            y1=j*sub_size
            x2=(sub_cnt-1-i)*sub_size
            y2=j*sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = a[x2+x][y2+y]

    return ans

# 부분 매트릭스를 한 칸으로 생각하고 매트릭스 전체 좌우반전.
def op6(a):
    global size
    sub_cnt = size // sub_size
    ans = list([0] * size for _ in range(size))

    for i in range(sub_cnt):
        for j in range(sub_cnt):
            # 기존 좌우반전 식의 b[i][j] = a[i][n-j-1] 과 같이 적용하여, 칸 간의 좌우반전
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = i * sub_size
            y2 = (sub_cnt - 1 - j) * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1 + x][y1 + y] = a[x2 + x][y2 + y]

    return ans

# 부분 매트릭스를 한 칸으로 생각하고 매트릭스 시계방향 90도 회전.
def op7(a):
    global size
    sub_cnt = size // sub_size
    ans = list([0] * size for _ in range(size))

    for i in range(sub_cnt):
        for j in range(sub_cnt):
            # 기존 좌우반전 식의 b[i][j] = a[n-1-j][i] 과 같이 적용하여, 칸 간의 우측 90도 회전
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = (sub_cnt - 1 - j) * sub_size
            y2 = i * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1 + x][y1 + y] = a[x2 + x][y2 + y]

    return ans

# 부분 매트릭스를 한 칸으로 생각하고 전체 매트릭스 반시계방향 90도 회전.
def op8(a):
    global size
    sub_cnt = size // sub_size
    ans = list([0] * size for _ in range(size))

    for i in range(sub_cnt):
        for j in range(sub_cnt):
            # 기존 좌우반전 식의 b[i][j] = a[j][n-1-i] 과 같이 적용하여, 칸 간의 좌측 90도 회전
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = j * sub_size
            y2 = (sub_cnt - 1 - i) * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1 + x][y1 + y] = a[x2 + x][y2 + y]

    return ans

# 매트릭스 시계방향 90도 회전
# 배열을 그룹 짓고 요소 rotate 후 다시 넣기
# rotate는 시간복잡도가 O(k)로, 회전횟수만큼의 시간복잡도만을 가진다.
# 그룹의 개수는 K=min(n,m)//2 다. 5x5 등으로 홀수일 경우, 가운데 1개는 돌지 않기에 회전 전과 후의 변화가 없다.
# 그룹별 요소는 윗줄, 오른쪽 줄, 아랫줄, 왼쪽 줄 순서로 큐에 담겨 회전된다.
# 수식은 위의 순서대로 a[k][j](k<=j<m-k), a[i][m-k-1](k<=i<n-k), a[n-k-1][j](k<=j<m-k), a[i][k](k<=i<n-k) 이다.
def rotate_group_clock_90(a):
    n=len(a)
    m=len(a[0])

    K=min(n,m)//2

    for k in range(K):
        q=deque()
        for j in range(k,m-k-1):
            q.append(a[k][j])
        for i in range(k,n-k-1):
            q.append(a[i][m-k-1])
        for j in range(m-k-1,k,-1):
            q.append(a[n-k-1][j])
        for i in range(n-k-1,k,-1):
            q.append(a[i][k])
        q.rotate(1)
        for j in range(k, m - k - 1):
            a[k][j]=q.popleft()
        for i in range(k, n - k - 1):
            a[i][m - k - 1]=q.popleft()
        for j in range(m - k - 1, k, -1):
            a[n - k - 1][j]=q.popleft()
        for i in range(n - k - 1, k, -1):
            a[i][k]=q.popleft()

    return a

# board 에서 테트리스하기(빈 칸 지나서 격자 내 맨 밑 칸으로 각 블록 이동)
# board 에서 'a'인 칸들 무시하고 블럭 떨어뜨리기
cnt = 1
while cnt:  # 움직이는 대상이 더 없어 0이 될 때까지
    cnt = 0  # 움직이는 대상의 수
    for x in range(n - 1):
        for y in range(m):
            if a[x][y] != "a" and a[x + 1][y] == "a":
                a[x][y], a[x + 1][y] = a[x + 1][y], a[x][y]
                cnt += 1

# 무한의 수 표현
INF = float('inf')
MAX=sys.maxsize

# 3차원 배열 선언하는 법
축 : z, 열 : m, 행 : n
[[[0]*z for j in range(m)] for i in range(n)]

# 요소가 빈 배열인 2차원 배열 생성
[[[] for _ in range(n)] for _ in range(n)] # 총들의 맵

# 달팽이 경로
# solution 1. 밖에서 안으로

# #  하,우,상,좌
dx=[1,0,-1,0]
dy=[0,1,0,-1]

x,y=0,0
d=0
a[x][y]=n**2

for v in range(n*n-1,0,-1):
    nx,ny=x+dx[d],y+dy[d]
    # 다음 칸이 범위 밖에 있거나 이미 값이 채워진 경우
    if not (0<=nx<n and 0<=ny<n) or a[nx][ny]!=0:
        # 방향 전환
        d=(d+1)%4
        # 전환된 방향의 전방 칸이 다음 칸
        nx, ny = x + dx[d], y + dy[d]
    a[nx][ny] = v
    if a[nx][ny]==tg:
        ans=[nx+1,ny+1]
    x, y = nx, ny

# solution 2. 안에서 밖으로

#    우,하,좌,상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

x = (n-1)//2
y = (n-1)//2
# 가운데 칸 채우기
a[x][y] = 1
num = 2

# 각 레이어는 3~n 범위의 홀수들만큼의 변의 길이를 가진다.
for size in range(3, n+1, 2):
    # 다음 레이어로 갈 때 위로 한 칸
    x += dx[3]
    y += dy[3]
    # 값 채우기
    a[x][y] = num
    # 값 증가
    num += 1
    # 이번 레이어를 우,하,좌,상 순서로 탐색
    for k in range(4):
        # (size-1)만큼 loop를 돌며 값을 채울 텐데,
        loop = size - 1
        # 오른쪽 방향으로는 (loop-1)만큼 loop를 돈다.
        if k == 0:
            loop -= 1
        # 해당 loop 만큼 이동하며 값을 채운 후 값을 증가시킨다.
        for i in range(loop):
            x += dx[k]
            y += dy[k]
            a[x][y] = num
            num += 1

# 주사위 굴리기
# 우
if d == 0:
    b[4] = a[6]
    b[3] = a[1]
    b[1] = a[4]
    b[6] = a[3]
    b[5] = a[5]
    b[2] = a[2]
# 하
elif d == 1:
    b[2] = a[6]
    b[1] = a[2]
    b[5] = a[1]
    b[6] = a[5]
    b[3] = a[3]
    b[4] = a[4]
# 좌
elif d == 2:
    b[6] = a[4]
    b[1] = a[3]
    b[4] = a[1]
    b[3] = a[6]
    b[5] = a[5]
    b[2] = a[2]
# 상
else:
    b[6] = a[2]
    b[2] = a[1]
    b[1] = a[5]
    b[5] = a[6]
    b[3] = a[3]
    b[4] = a[4]

a = b

# BFS 최단 경로 저장
def bfs1(x,y,ex,ey):
    global a
    # 경로 딕셔너리
    parent=dict()
    q=deque()
    start = [x, y]
    q.append(start)
    d=[[-1]*n for _ in range(n)]
    d[x][y]=0

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            # 격자 내, 출입 금지 아니며, 미탐색 지역이면 탐색
            if 0<=nx<n and 0<=ny<n and a[nx][ny]!=3 and d[nx][ny]==-1:
                d[nx][ny]=d[x][y]+1
                q.append([nx,ny])
                # 다음 위치 key 가 현재 위치를 value로 갖도록 경로 딕셔너리에 정보 추가
                parent[(nx,ny)]=(x,y)
    # 최단 경로
    trace = []
    current = (ex,ey)
    start=tuple(start)
    while current != start:
        trace.append(current)
        current = parent[current]
    trace.append(start)
    # 시작점부터 목적지까지
    trace.reverse()
    # 시작점 바로 다음 위치가 다음 갈 곳
    ans=trace[1]
    return ans