# 해설 : https://carnival.tistory.com/manage/posts/

n=int(input())
mod = 9901

d=[[0] * 3 for _ in range(n+1)]

d[1][0] = 1
d[1][1] = 1
d[1][2] = 1

for i in range(2,n+1):
    d[i][0] = d[i-1][0] + d[i-1][1] + d[i-1][2]
    d[i][0] %= mod
    d[i][1] = d[i-1][0] + d[i-1][2]
    d[i][1] %= mod
    d[i][2] = d[i-1][0] + d[i-1][1]
    d[i][2] %= mod

print(sum(d[n])%mod)