 # 조합 문제. N개 중 M개를 선택하여 중복 허용 X, 순서 상관하며 사용. 즉, 순서가 달라도 같은 요소로 구성되어 있으면 같은 집합
# 순열 문제. N개 중 M개를 선택하여 중복 허용 X, 순서 상관 없이 사용. 즉, 순서가 다르고 같은 요소로 구성되어 있으면 다른 집합
# 중복 순열 문제. N개 중 M개를 선택하여 중복 허용 O, 순서 상관 없이 사용. 즉, 순서가 다르고 같은 요소로 구성되어 있으면 다른 집합

1. board = [list(input()) for _ in range(n)]
: 정수 배열을 행렬로 입력
CCP
CCP
PPC

[['C', 'C', 'P'], ['C', 'C', 'P'], ['P', 'P', 'C']]

% 주의! input = sys.stdin.readline 으로 설정하면, 엔터(/n)도 같이 입력되니 주의
ex ) [['C', 'C', 'P', '\n'], ['C', 'C', 'P', '\n'], ['P', 'P', 'C', '\n']]

# 리스트 슬라이싱
1. a[N:M]
a[N] <= x < a[M]
a[N] <= x <= a[M-1]
N을 포함한 인덱스 부터 M을 포함하지 않는 인덱스 까지를 자르는 기능을 합니다.
특이사항! M이 실제 리스트의 크기를 넘어서는 수이면, 인덱스 오류가 발생하는 것이 아니라, 자동으로 리스트의 맨 마지막 요소까지로 인식한다.

2. a[:M]
a[0] <= x < a[M]
a[0] <= x <= a[M-1]

3. a[N:]
a[N] <= x < a[len(a)]
a[N] <= x <= a[len(a) - 1]
len(a)는 리스트의 길이를 말합니다.

4. a[:] 이처럼 양쪽을 비워서 슬라이싱을 한다는 것은 리스트 전체를 복사하는것과 동일합니다.
a[0] <= x < a[len(a)]
a[0] <= x <= a[len(a) - 1]

# reverse
temp = temp[::-1]

# 1차원 배열 시계/반시계 방향 회전
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

# 정사각형 매트릭스 조작
# 매트릭스 상하반전
def op1(a):
    n=len(a)
    b=[[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            b[i][j] = a[n-1-i][j]

    return b

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

# 매트릭스 좌우반전
def op2(a):
    n=len(a)
    b=[[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            b[i][j] = a[i][n-j-1]

    return b

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

# 매트릭스 시계방향 90도 회전
def op3(a):
    n = len(a)
    b = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            b[i][j] = a[n-1-j][i]

    return b

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

# 매트릭스 반시계방향 90도 회전 = 시계방향 90도로 3번 회전
def op4(a):
    n = len(a)
    b = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            b[i][j] = a[j][n-1-i]

    return b

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

# 상하 반전
n, m = 4, 6
arr = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
temp = [[0] * m for _ in range(n)]

# 1. 반복문
for i in range(n):
    temp[i] = arr[n - 1 - i]

# 2. 문자열 슬라이싱
arr = arr[::-1]

# 좌우 반전
n, m = 4, 6
arr = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
temp = [[0] * m for _ in range(n)]

# 1. 반복문
for i in range(n):
    for j in range(m):
        temp[i][j] = arr[i][m - 1 - j]

# 2. 문자열 슬라이싱
for i in range(n):
    arr[i] = arr[i][::-1]

# 무한의 수 표현
INF = float('inf')

3차원 배열 선언하는 법
축 : z, 열 : m, 행 : n
[[[0]*z for j in range(m)] for i in range(n)]