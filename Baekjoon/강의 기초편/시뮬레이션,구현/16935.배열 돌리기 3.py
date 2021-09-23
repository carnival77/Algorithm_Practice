import sys

input = sys.stdin.readline

n,m,r= map(int,input().split())

a=[]

for i in range(n):
    a.append(list(map(int,input().split())))

cmds = list(map(int,input().split()))

def op1(a):
    # 1번 연산
    n=len(a)
    m=len(a[0])
    b = list([0] * m for _ in range(n))  # a 모두에 0을 대신 채운 b. n 행 m 열
    for i in range(n):
        for j in range(m):
            # 상하 대칭으로 행을 바꾼다. : i = n-1-i
            next_i = (n-1) - i
            b[i][j] = a[next_i][j]
    return b

def op2(a):
    # 2번 연산
    n=len(a)
    m=len(a[0])
    b = list([0] * m for _ in range(n))  # a 모두에 0을 대신 채운 b. n 행 m 열
    for i in range(n):
        for j in range(m):
            # 좌우 대칭으로 열을 바꾼다. : j = m-1-j
            next_j = (m-1) - j
            b[i][j] = a[i][next_j]
    return b

# 우측 90도 회전
def op3(a):
    # 90도 회전은 b를 n 행 m 열 -> m 행 n 열로
    # 3번 연산
    n=len(a)
    m=len(a[0])
    b = list([0] * n for _ in range(m))  # a 모두에 0을 대신 채운 b. m 행 n 열
    for i in range(m):
        for j in range(n):
            # 오른쪽으로 90도 회전시킨다.
            # 1) b[i][j] = a[][]
            # 2) b의 i번째 행 = a의 i번째 열 : b[i][j] = a[][i]
            # 3) b의 i번째 행의 j의 순서 = a의 i번째 열의 거꾸로순 : b[i][j] = a[n-1-j][i]
            b[i][j] = a[n-1-j][i]
    return b

# 좌측 90도 회전
def op4(a):
    # 90도 회전은 b를 n 행 m 열 -> m 행 n 열로
    # 4번 연산
    n=len(a)
    m=len(a[0])
    b = list([0] * n for _ in range(m))  # a 모두에 0을 대신 채운 b. m 행 n 열
    for i in range(m):
        for j in range(n):
            # 왼쪽으로 90도 회전시킨다.
            b[i][j] = a[j][m-1-i]
    return b

def op5(a):
    # 5번 연산
    n=len(a)
    m=len(a[0])
    b = list([0] * m for _ in range(n))  # a 모두에 0을 대신 채운 b. m 행 n 열
    int_n = int(n/2)
    int_m = int(m/2)
    for i in range(int_n):
        for j in range(int_m):
            # 시계방향으로 1칸씩 이동
            # 1번 자리 기준으로 수행
            # 1 -> 2
            b[i][j+int_m] = a[i][j]
            # 2 -> 3
            b[i+int_n][j+int_m] = a[i][j+int_m]
            # 3 -> 4
            b[i+int_n][j] = a[i+int_n][j+int_m]
            # 4 -> 1
            b[i][j] = a[i+int_n][j]

    return b

def op6(a):
    # 6번 연산
    n=len(a)
    m=len(a[0])
    b = list([0] * m for _ in range(n))  # a 모두에 0을 대신 채운 b. m 행 n 열
    int_n = int(n/2)
    int_m = int(m/2)
    for i in range(int_n):
        for j in range(int_m):
            # 반시계방향으로 1칸씩 이동
            # 1번 자리 기준으로 수행
            # 2 -> 1
            b[i][j] = a[i][j+int_m]
            # 3 -> 2
            b[i][j+int_m] = a[i+int_n][j+int_m]
            # 4 -> 3
            b[i+int_n][j+int_m] = a[i+int_n][j]
            # 1 -> 4
            b[i+int_n][j] = a[i][j]
    return b

# 함수 배열을 만든다.
ops = [op1,op2,op3,op4,op5,op6]
for cmd in cmds:
    a = ops[cmd-1](a)

for row in a:
    print(*row,sep=' ')
