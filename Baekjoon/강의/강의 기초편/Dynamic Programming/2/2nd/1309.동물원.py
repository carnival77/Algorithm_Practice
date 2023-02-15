n=int(input())
d=[[0]*3 for _ in range((n+1))] # 2xn의 배열에 사자를 배치하는 경우의 수.
# d[n][0],d[n][1],d[n][1] : 2xn의 배열의 n번째 줄의 왼쪽, 오른쪽에 사자를 배치하거나, 배치하지 않는 경우의 수
mod=9901
d[1][0]=1
d[1][1]=1
d[1][2]=1

for i in range(2,n+1):
    d[i][0]=d[i-1][1]+d[i-1][2]+d[i-1][0]
    d[i][0]%=mod
    d[i][1]=d[i-1][0]+d[i-1][2]
    d[i][1]%=mod
    d[i][2]=d[i-1][0]+d[i-1][1]
    d[i][2]%=mod

print(sum(d[n])%mod)