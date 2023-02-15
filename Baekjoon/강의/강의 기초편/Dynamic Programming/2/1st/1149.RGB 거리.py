# 해설 : https://carnival.tistory.com/69

n=int(input())

a = [[0,0,0]] + [list(map(int,input().split()))for _ in range(n)]

d=[[0,0,0] for _ in range(n+1)]

for i in range(1,n+1):
    d[i][0] = min(d[i-1][1],d[i-1][2])+a[i][0]
    d[i][1] = min(d[i-1][0],d[i-1][2])+a[i][1]
    d[i][2] = min(d[i-1][0],d[i-1][1])+a[i][2]

print(min(d[n][0],d[n][1],d[n][2]))