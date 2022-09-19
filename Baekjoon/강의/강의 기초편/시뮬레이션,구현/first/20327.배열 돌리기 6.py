import sys

input = sys.stdin.readline

n,r = map(int,input().split())

a=[list(map(int,input().split())) for _ in range(2**n)]

size =  2**n

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

# 매트릭스 반시계방향 90도 회전
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

# sx,sy 는 시작지점
def op_1_4(a,sx,sy,sub_size,k):

    ans=list([0]*sub_size for _ in range(sub_size))

    # 시작지점부터 sub_size만큼의 칸을 떼어서
    for i in range(sub_size):
        for j in range(sub_size):
            ans[i][j] = a[sx+i][sy+j]

    # op 적용 후
    if k==1: ans = op1(ans)
    elif k==2 : ans=op2(ans)
    elif k==3 : ans=op3(ans)
    else: ans=op4(ans)

    # a의 그 부분에 다시 넣기
    for i in range(sub_size):
        for j in range(sub_size):
            a[sx+i][sy+j] = ans[i][j]

for _ in range(r):
    k,l = map(int,input().split())
    sub_size = 2**l
    if 1<=k<=4:
        for i in range(0,size,sub_size):
            for j in range(0,size,sub_size):
                op_1_4(a,i,j,sub_size,k)
    else:
        if k==5: a=op5(a)
        elif k==6 : a=op6(a)
        elif k==7 : a=op7(a)
        else: a=op8(a)

for i in range(len(a)):
    print(" ".join(map(str,a[i])))