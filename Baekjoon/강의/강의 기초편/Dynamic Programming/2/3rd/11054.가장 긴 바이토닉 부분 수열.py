# solution 1.
# dp1[i] = a[i]에서 끝나는 가장 긴 증가하는 부분 수열의 길이와,
# dp2[i] = a[i]부터 시작하는 가장 긴 감소하는 부분 수열의 길이 찾은 다음,
# dp1[i] + dp2[i] - 1 한 값을 찾는다. ( 중복이 되기 때문 )

n=int(input())
a=list(map(int,input().split()))

dp1=[0]*n
dp2=[0]*n
dp=[0]*n

# a[i]에서 끝나는 가장 긴 증가하는 부분 수열의 길이
for i in range(n):
    dp1[i]=1
    for j in range(i):
        if a[j]<a[i]:
            dp1[i]=max(dp1[i],dp1[j]+1)
        # if a[j] < a[i] and dp1[j]+1 > dp1[i]:
        #     dp1[i]=dp1[j]+1

# a[i]부터 시작하는 가장 긴 감소하는 부분 수열의 길이
for i in range(n-1,-1,-1):
    dp2[i]=1
    for j in range(i+1,n):
        if a[j]<a[i]:
            dp2[i]=max(dp2[i],dp2[j]+1)
        # if a[j]>a[i] and dp2[j]+1 > dp2[i]:
        #     dp2[i]=dp2[j]+1

for i in range(n):
    dp[i]=dp1[i]+dp2[i]-1

print(max(dp))

# solution 2.
# dp1[i] = a[i]에서 끝나는 가장 긴 증가하는 부분 수열의 길이와,
# dp2[i] = a를 거꾸로 나열한 reversed_a 배열의 a[i]에서 끝나는 가장 긴 증가하는 부분 수열의 길이를 찾은 다음,
# dp1[i] + reversed_dp2[i] - 1 한 값을 찾는다. ( 중복이 되기 때문 )
# reversed_dp2[i] 인 이유는 dp2[i] 를 reverse 해야 a[i]부터 시작하는 가장 긴 감소하는 부분 수열의 길이가 되기 때문

n=int(input())
a=list(map(int,input().split()))

d1=[0]*(n)
d2=[0]*(n)
ans=0

reversed_a=a[::-1]

for i in range(n):
    d1[i]=1
    d2[i]=1
    for j in range(i):
        if a[j]<a[i]:
            d1[i]=max(d1[i],d1[j]+1)
        if reversed_a[j]<reversed_a[i]:
            d2[i]=max(d2[i],d2[j]+1)

reversed_d2=d2[::-1]

for i in range(n):
    ans=max(ans,d1[i]+reversed_d2[i]-1)

print(ans)