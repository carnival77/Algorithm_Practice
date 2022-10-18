d=[[0]*10 for _ in range(101)] # d[i][j]= 길이가 i이고 마지막 자리의 수가 j인 계단수의 개수
mod=1000000000

for i in range(1,101):
    for j in range(10):
        if i==1:
            if j==0:
                d[i][j]=0
            else:
                d[i][j]=1
        else:
            if j==0:
                d[i][j] = d[i - 1][j + 1]
            elif j==9:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j]=d[i-1][j-1]+d[i-1][j+1]
        d[i][j]%=mod
n=int(input())
print(sum(d[n])%mod)