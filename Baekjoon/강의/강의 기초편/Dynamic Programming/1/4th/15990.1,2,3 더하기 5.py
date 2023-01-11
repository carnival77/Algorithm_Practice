MAX=100001
mod=1000000009
t=int(input())
d=[[0]*4 for _ in range(MAX)]
d[1][1]=1
d[2][2]=1
d[3][3]=1
d[3][2]=1
d[3][1]=1

for i in range(4,MAX):
    for j in range(1,4):
        if j==1:
            d[i][j]=d[i-1][2]+d[i-1][3]
        elif j==2:
            d[i][j]=d[i-2][1]+d[i-2][3]
        else:
            d[i][j]=d[i-3][1]+d[i-3][2]
        d[i][j]%=mod

for i in range(t):
    n=int(input())
    print(sum(d[n])%mod)