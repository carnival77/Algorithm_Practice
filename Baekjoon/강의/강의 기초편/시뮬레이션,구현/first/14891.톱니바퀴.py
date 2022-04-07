n=4
a=[list(input()) for _ in range(n)]
k=int(input())
for _ in range(k):
    tg,dir = map(int,input().split())
    tg = tg-1
    d=[0]*n # 각 톱니의 회전 여부. 0 = 회전 X. 1 = 시계방향, -1 = 반시계방향
    d[tg]=dir
    # 왼쪽 톱니바퀴 연쇄적으로 구하기
    for i in range(tg-1,-1,-1):
        if a[i][2] != a[i+1][6]:
            d[i] = -d[i+1]
        else:
            break
    # 오른쪽 톱니바퀴 연쇄적으로 구하기
    for i in range(tg+1,n):
        if a[i-1][2] != a[i][6]:
            d[i] = -d[i-1]
        else:
            break
    # 회전 적용
    for i in range(n):
        if d[i]==0:
            continue
        # 시계방향
        elif d[i]==1:
            temp = a[i][7]
            for j in range(7, 0, -1):
                a[i][j] = a[i][j-1]
            a[i][0] = temp
        # 반시계방향
        elif d[i]==-1:
            temp=a[i][0]
            for j in range(7):
                a[i][j] = a[i][j+1]
            a[i][7] = temp

ans=0
for i in range(n):
    if a[i][0] == '1':
        ans = ans + 2 ** i
print(ans)