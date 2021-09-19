n,r = map(int,input().split())

a=[list(map(int,input().split())) for _ in range(2**n)]

cmds = []

for _ in range(r):
    cmds.append((map(int,input().split())))

# 상하반전
def op1(a):
    n=len(a)
    m=len(a[0])
    b=[[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            b[i][j] = a[n-1-i][j]

# 좌우반전
def op2(a):
    n=len(a)
    m=len(a[0])
    b=[[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][m-j-1]

# 우측 90도 회전
def op3(a):
    n = len(a)
    m = len(a[0])
    b = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            b[i][j] = a[n-1-j][i]

# 좌측 90도 회전
def op4(a):
    n = len(a)
    m = len(a[0])
    b = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            b[i][j] = a[j][m-1-i]

def op5():
    pass

def op6():
    pass

def op7():
    pass

def op8():
    pass

ops = [op1,op2,op3,op4,op5,op6,op7,op8]