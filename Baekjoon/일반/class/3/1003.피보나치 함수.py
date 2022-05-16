#solution 1. topdown 방식
# dp=[-1]*41
# dp[0]=0
# dp[1]=1
#
# def fibonacci(n):
#     global dp
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     elif dp[n]!=-1:
#         return dp[n]
#     else:
#         dp[n]=fibonacci(n-1)+fibonacci(n-2)
#         return dp[n]
#
# t=int(input())
# for _ in range(t):
#     n=int(input())
#     fibonacci(n)
#     if n==0:
#         print("1 0")
#     else:
#         print(dp[n-1],dp[n])

#solution 2. bottom up 방식
dp=[[1,0],[0,1]]
t=int(input())
q=list(int(input()) for _ in range(t))

for i in range(2,max(q)+1):
    dp.append([dp[i-2][0]+dp[i-1][0],dp[i-2][1]+dp[i-1][1]])
for i in q:
    print(dp[i][0],dp[i][1])