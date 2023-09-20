import sys
input=sys.stdin.readline
MAX=int(1e9)

n=int(input())
a=[[0]*(n+1)]
a+=[[0]+list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

ans=MAX

def divide(r1,r2,c1,c2,no):
    global b

    for r in range(r1,r2):
        if no%2!=0:
            for c in range(c1, c2):
                if b[r][c]==5:
                    break
                if b[r][c] == 0:
                    b[r][c] = no
        else:
            for c in range(c2-1,c1-1,-1):
                if b[r][c]==5:
                    break
                if b[r][c]==0:
                    b[r][c]=no

def cal():
    s=[0]*5
    for no in range(1,6):
        for x in range(1,n+1):
            for y in range(1,n+1):
                if b[x][y]==no:
                    s[no-1]+=a[x][y]
    return s

for x in range(1,n-1):
    for y in range(2,n):
        for d1 in range(1,n):
            for d2 in range(1,n):
                # 기준점 (x, y)와 경계의 길이 d1, d2를 정한다. (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
                if x+d1+d2<=n and 1<=y-d1 and y-d1<y and y<y+d2 and y+d2<=n:
                # if x==3 and y==3 and d1==1 and d2==1:
                    b = [[0] * (n + 1) for _ in range(n + 1)]
                    # 다음 칸은 경계선이다. 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.
                    for i in range(d1+1):
                        b[x+i][y-i]=5
                    for i in range(d2+1):
                        b[x+i][y+i]=5
                    for i in range(d2+1):
                        b[x+d1+i][y-d1+i]=5
                    for i in range(d1+1):
                        b[x+d2+i][y+d2-i]=5
                    # 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다
                    divide(1,x+d1,1,y+1,1)
                    divide(1, x + d2+1, y+1, n+1, 2)
                    divide(x+d1, n+1, 1, y-d1+d2, 3)
                    divide(x + d2+1, n + 1, y-d1+d2, n+1, 4)
                    # 경계선의 안에 포함되어있는 곳은 5번 선거구이다.
                    for i in range(1,n+1):
                        for j in range(1,n+1):
                            if b[i][j]==0:
                                b[i][j]=5
                    one,two,three,four,five=cal()
                    ans=min(ans,max(one,two,three,four,five)-min(one,two,three,four,five))

print(ans)