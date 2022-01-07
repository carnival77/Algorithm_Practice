n=int(input())
a=list(map(int,input().split()))

dp=[-1]*(n)

dp[0]=0

for i in range(n):
    for j in range(0,i):
        if dp[j] != -1 and i-j <= a[j]:
            if dp[i]==-1 or dp[i]>dp[j]+1:
                dp[i]=dp[j]+1

print(dp[n-1])

# for i in range(n):
#     if d[i]==-1: continue
#     for j in range(1,a[i]+1):
#         if i+j>=n:
#             break
#         if

# for i in range(n):
#     for j in range(1,a[i]+1):
#         if i+j<=n:
#             break
#         dp
#
# print(d[n-1])