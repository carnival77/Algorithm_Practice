n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]
d=[[0]*3 for _ in range(n+1)] # i번째 집을 j로 칠했을 때 전체 최소 비용(j : 0(빨), 1(파), 2(초))

d[1][0]=a[0][0]
d[1][1]=a[0][1]
d[1][2]=a[0][2]

for i in range(2,n+1):
    d[i][0]=min(d[i-1][1],d[i-1][2])+a[i-1][0]
    d[i][1]=min(d[i-1][0],d[i-1][2])+a[i-1][1]
    d[i][2]=min(d[i-1][0],d[i-1][1])+a[i-1][2]

print(min(d[n][0],d[n][1],d[n][2]))