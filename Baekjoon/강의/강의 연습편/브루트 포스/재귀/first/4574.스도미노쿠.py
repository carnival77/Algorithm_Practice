#!/usr/bin/env Python
# coding=utf-8
from itertools import permutations
def convert(p):
    return ord(p[0])-ord('A'), int(p[1])-1
# 작은 정사각형은 총 9개가 있으며, make_square 함수는 (x,y)를 받고 해당 칸이 속한 작은 정사각형의 번호를 반환한다.
def make_square(x,y):
    return (x//3)*3 + y//3
# 행, 열, 3x3 크기의 정사각형 체크
def check(x,y,n,what):
    row[x][n]=col[y][n]=square[make_square(x,y)][n]=what
def can(x,y,n):
    return not row[x][n] and not col[y][n] and not square[make_square(x,y)][n]
def recur(z):
    # recur 함수는 z==81이 되어 마지막 칸까지 탐색을 마치는 경우 답을 출력하고 True를 리턴한다.
    if z==81:
        for r in a:
            print(''.join(map(str,r)))
        return True
    x,y=divmod(z,n)
    # 0이 아닌 경우 다음 칸을 탐색한다.
    if a[x][y]!=0:
        return recur(z+1)
    # 해당 칸에서 만들 수 있는 가로, 세로 2개의 도미노 중 행, 열, 작은 정사각형 모두에 없는 도미노를 넣어본다.
    for k in range(2):
        nx,ny=x+dx[k],y+dy[k]
        if not (0<=nx<n and 0<=ny<n):
            continue
        if a[nx][ny]!=0:
            continue
        for i,j in permutations(arr,2):
            if domino[i][j]:
                continue
            if can(x,y,i) and can(nx,ny,j):
                a[x][y]=i
                a[nx][ny]=j
                check(x,y,i,True)
                check(nx,ny,j,True)
                domino[i][j]=domino[j][i]=True
                # 경우의 수들 중 마지막 칸까지 탐색을 성공한 경우 True가 반환되므로, 아래의 제거 과정을 다시 밟지 않고 recur 함수가 종료되도록 True를 반환한다.
                if recur(z + 1): return True
                a[x][y]=0
                a[nx][ny]=0
                check(x,y,i,False)
                check(nx,ny,j,False)
                domino[i][j]=domino[j][i]=False
    # 마지막 칸까지 탐색을 마치지도, 이번 칸이 0인 경우도 아닌 경우, 실패한 탐색이다.
    return False
n=9
dx=[0,1]
dy=[1,0]
tc=1
arr=list(i for i in range(1,10))
while True:
    m=int(input())
    if m==0:
        break
    a=[[0]*9 for _ in range(9)]
    # 빈 칸에 넣을 숫자를 판별하기 위해서는 해당 칸이 속한 행, 열, 3x3 크기의 정사각형 이 3개에 존재하는 숫자를 살펴야 한다.
    # 이 3개를 row, col, sqaure 배열로 설정하여, 각 숫자를 포함하고 있는지를 Boolean형으로 나타내게 한다.
    # 가령 row[i][j] = True 는 i번째 행은 j라는 숫자를 포함하고 있다는 뜻이다.
    row=[[False] * 10 for _ in range(10)]
    col=[[False] * 10 for _ in range(10)]
    square = [[False] * 10 for _ in range(10)]
    domino=[[False] * 10 for _ in range(10)]
    for _ in range(m):
        n1,p1,n2,p2=input().split()
        n1,n2=int(n1),int(n2)
        x1,y1=convert(p1)
        x2,y2=convert(p2)
        domino[n1][n2]=domino[n2][n1]=True
        a[x1][y1]=n1
        a[x2][y2]=n2
        check(x1,y1,n1,True)
        check(x2,y2,n2,True)
    for i,np in enumerate(input().split()):
        x,y=convert(np)
        a[x][y]=i+1
        check(x,y,i+1,True)
    print("Puzzle %d" %tc)
    tc+=1
    recur(0)