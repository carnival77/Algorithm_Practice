# 가장 긴 바이토닉 부분 수열의 길이 = 가장 긴 증가하는 부분 수열의 길이(d) + 가장 긴 감소하는 부분 수열의 길이(d2) - 1
# -> d[i] : a[i]까지의 수열 중 가장 긴 증가하는 부분 수열의 길이, d2[i] : a[i]부터의 수열 중 가장 긴 감소하는 부분 수열의 길이
# ans=max(d[i]+d2[i]-1)

n=int(input())
a=list(map(int,input().split()))

d=[1]*n # d[i] : a[i]까지의 수열 중 가장 긴 증가하는 부분 수열의 길이

for i in range(n):
    for j in range(i):
        if a[j]<a[i]:
            d[i]=max(d[i],d[j]+1)

d2=[1]*n # d2[i] : a[i]부터의 수열 중 가장 긴 감소하는 부분 수열의 길이

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if a[j]<a[i]:
            d2[i]=max(d2[i],d2[j]+1)

ans=0
for i in range(n):
    ans=max(ans,d[i]+d2[i]-1)
print(ans)