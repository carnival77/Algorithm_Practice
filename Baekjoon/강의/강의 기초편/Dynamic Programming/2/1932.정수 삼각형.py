n=int(input())

# d[i][j] = (i,j)에 도착했을 때의 최댓값.
# d[i][j] = (i-1)층까지의 최댓값에 a[i][j]을 더한 값
d=[[0]*n for _ in range(n)]

a = [list(map(int,input().split())) for _ in range(n)]

d[0][0] = a[0][0]

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            # 대각선 오른쪽 위로부터만
            d[i][j] = d[i-1][j] + a[i][j]
        elif 0<j<i:
            # 대각선 왼쪽, 오른쪽 위 두 방향 모두로부터
            d[i][j] = max(d[i-1][j],d[i-1][j-1]) + a[i][j]
        else:
            # 대각선 왼쪽 위로부터만
            d[i][j] = d[i-1][j-1] + a[i][j]

# (n-1) 층에 저장된 값들 중 최댓값
print(max(d[n-1]))