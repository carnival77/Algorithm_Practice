n=int(input())
a=list(map(int,input().split()))

dp=[-1]*(n) # dp[i] = i번 칸에 도착할 수 있는 최소 점프 횟수. -1(아직 도착하지 않은 경우)로 초기화한다.

dp[0]=0

# solution 1.

# dp[i] = dp[j]+1. : j번 칸에 도착한 후 1번 더 가서 i번 칸에 도착한다.
# 이때 i번 칸에 도착하기 전인 j번 칸이 어떤 칸일지 알 수 없다. 따라서 i보다 작은 칸들을 j번 칸이라 가정하고 탐색한다.
# j -> i 번으로 갈 수 있으려면 i-j <= a[j] 가 되어야 한다.
# dp[i] = min(dp[j]) + 1 ( j < i , i - j <= a[j] )

for i in range(1,n):
    for j in range(0,i):
        if dp[j] != -1 and i-j <= a[j]: # j 에 도착할 수 있는가, 점프를 할 수 있는가?
            if dp[i]==-1 or dp[i]>dp[j]+1:
                dp[i]=dp[j]+1

print(dp[n-1])

#solution 2.

# d[i+j] = d[i] + 1 : i+j 번째 칸은 i 번째 칸에서 a[j]에 있는 수를 더한 만큼의 칸으로 1번 이동한 것이다.
# i 번 칸에서, 1부터 그 i 번 칸에 쓰인 수까지를 j라 하고, i+j 가 n을 넘지 않는다면, dp[i+j]를 min값으로 초기화한다.

for i in range(n):
    if dp[i]==-1: continue
    for j in range(1,a[i]+1):
        if i+j>=n:
            break
        if dp[i+j] == -1 or dp[i+j] > dp[i]+1:
            dp[i+j] = dp[i]+1

print(dp[n-1])