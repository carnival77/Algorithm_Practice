# n = int(input())
# a = list(map(int,input().split()))
# d = [0]*n
# for i in range(n):
#     d[i] = 1
#     for j in range(i):
#         if a[j] < a[i] and d[j]+1 > d[i]:
#             d[i] = d[j]+1
# print(max(d))










+

















n=int(input())
a=list(map(int,input().split()))

dp=[0]*n

for i in range(n):
    dp[i]=1
    for j in range(i):
        if a[j]<a[i] and dp[j]+1 > dp[i]:
            dp[i]=dp[j]+1

print(max(dp))

