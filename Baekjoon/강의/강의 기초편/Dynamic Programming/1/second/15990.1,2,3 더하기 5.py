t=int(input())

MAX = 100000

mod = 1000000009

d=[[0] * 4 for _ in range(MAX+1)] # 1,2,3으로 정수 N을 만들되 연속 사용은 배제하는 모든 방법의 수
# d[i][j]=j를 마지막으로 사용하여 i를 만드는 방법의 수

for i in range(1,MAX+1):
    if i>=1:
        d[i][1] = d[i-1][2] + d[i-1][3]
        if i==1:
            d[i][1]=1
    if i>=2:
        d[i][2] = d[i-2][1] + d[i-2][3]
        if i==2:
            d[i][2]=1
    if i>=3:
        d[i][3] = d[i-3][1] + d[i-3][2]
        if i==3:
            d[i][3]=1
    d[i][1] %= mod
    d[i][2] %= mod
    d[i][3] %= mod

for _ in range(t):
    n=int(input())
    print(sum(d[n])%mod)