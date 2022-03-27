import sys

input = sys.stdin.readline

# def print_a(a):
#     for i in range(len(a)):
#         print(a[i])
#     print()

def cnt_num(a):
    b1 = []
    for i in range(1, 101):
        if a.count(i) > 0:
            b1.append((i, a.count(i)))
    return b1

def sort_func(a):
    return sorted(a,key = lambda x : (x[1],x[0]))

def make_list(a):
    temp = []
    for i in a:
        x, y = i
        temp.append(x)
        temp.append(y)
    return temp

def sort_arr(a):
    return make_list(sort_func(cnt_num(a)))

def left_90(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = a[j][m-i-1]
    return ans

def right_90(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = a[n-j-1][i]
    return ans

def process_R(a):
    temp=[]
    for row in a:
        temp.append(sort_arr(row))
    r=len(temp)
    c=0
    for row in temp:
        c=max(c,len(row))
    b=list([0] * c for _ in range(r))
    for i in range(r):
        for j in range(len(temp[i])):
            b[i][j] = temp[i][j]
    return b

def process_C(a):
    # 좌로 90도 회전
    a = left_90(a)
    a=process_R(a)
    # 우로 90도 회전
    a=right_90(a)
    return a

r,c,k = map(int,input().split())
r-=1
c-=1

time,n,m=0,3,3

a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))

# 종료 조건
if a[r][c] == k:
    print(0)
    sys.exit(0)

for time in range(1,101):
    # R or C ?
    # R
    if n >= m:
        a=process_R(a)
        n=len(a)
        m=len(a[0])
    # C
    else:
        a=process_C(a)
        n = len(a)
        m = len(a[0])
    # 종료 조건
    # print_a(a)
    # print(len(a),r,len(a[0]),c)
    if len(a)<=r or len(a[0])<=c:
        continue
    else:
        if a[r][c] == k:
            print(time)
            break

if time==101:
    print(-1)