# n = int(input())
# a = list(map(int,input().split()))
# d = [0]*n
# for i in range(n):
#     d[i] = 1
#     for j in range(i):
#         if a[j] < a[i] and d[j]+1 > d[i]:
#             d[i] = d[j]+1
# print(max(d))










n=int(input())
a=list(map(int,input().split()))

# dp[i] = a[1]...a[i] 까지의 수열이 있을 때, a[i]를 마지막으로 하는 가장 긴 증가하는 부분수열의 길이
dp=[0]*n

# 조건에 맞으려면, a[1] ... a[j],a[i] 수열이 있으면, j<i , a[j] < a[i]. 이어야 한다.
# a[j]<a[i] 인 상태에서, d[j] 에 a[i] 1개를 추가한 길이가 d[i]보다 크면, d[i]는 d[j] 에 a[i] 1개를 더한 길이로 변경해준다.

for i in range(n):
    dp[i]=1
    for j in range(i):
        if a[j]<a[i] and dp[j]+1 > dp[i]:
            dp[i]=dp[j]+1

print(max(dp))