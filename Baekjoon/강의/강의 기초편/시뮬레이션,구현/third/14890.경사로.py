import sys
input=sys.stdin.readline

n,l=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=0
c=[]

def check(x,y):
    global c

    res=True
    if a[x][y+1]==a[x][y]+1:
        for i in range(l):
            if not (0<=y-i<n) or a[x][y-i]!=a[x][y] or c[x][y-i]:
                res=False
                break
        if res:
            for i in range(l):
                c[x][y-i]=True
    elif a[x][y+1]==a[x][y]-1:
        for i in range(l):
            if not (0<=y+1+i<n) or a[x][y+1+i] != a[x][y+1] or c[x][y+1+i]:
                res = False
                break
        if res:
            for i in range(l):
                c[x][y+1+i] = True
    else:
        res=False

    return res

def process(a):
    global ans,c

    c = [[False] * n for _ in range(n)]

    for x in range(n):
        ok = True
        for y in range(n - 1):
            if a[x][y] == a[x][y + 1]:
                continue
            else:
                ok = check(x, y)
                if not ok:
                    break
        if ok:
            ans += 1

# 행 체크
process(a)
# 열 체크
# 행렬 변환
a=list(map(list,zip(*a)))
process(a)
print(ans)