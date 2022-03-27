n=int(input())
a=list(map(int,input().split()))

# dp[i] = a[1]...a[i] 까지의 수열이 있을 때, a[i]를 마지막으로 하는 가장 합이 큰 증가 부분 수열의 합
dp=[0]*n

# 조건에 맞으려면, a[1] ... a[j],a[i] 수열이 있으면, j<i , a[j] < a[i]. 이어야 한다.
# a[j]<a[i] 인 상태에서, d[j] 에 a[i] 1개를 추가한 값이 d[i]보다 크면, d[i]는 d[j] 에 a[i]을 더한 값으로 변경해준다.

for i in range(n):
    dp[i]=a[i]
    for j in range(i):
        if a[j]<a[i] and dp[j]+a[i] > dp[i]:
            dp[i]=dp[j]+a[i]

print(max(dp))