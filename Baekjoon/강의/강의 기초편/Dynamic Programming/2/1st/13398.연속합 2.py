n=int(input())
a=list(map(int,input().split()))
d1=a # 수열 a의 각 인덱스까지의 최대 연속합을 담는다. d1[i] : i번째 수에서 끝나는 최대 연속합
d2=a[::-1] # 수열 a의 각 인덱스부터의 최대 연속합을 담는다. d2[i] : i번째 수에서 시작하는 최대 연속합
# i번째 수를 제거하면 i-1번째 수와 i+1번째 수가 연속하게 된다.
# 따라서, d1[i-1] + d2[i+1] 이 i번째 수를 제거했을 때의 최대 연속합이 된다.

for i in range(1,n):
    if d1[i]<d1[i]+d1[i-1]:
        d1[i]=d1[i]+d1[i-1]
    if d2[i] < d2[i] + d2[i - 1]:
        d2[i] = d2[i] + d2[i - 1]
d2.reverse()
ans=max(d1)
for i in range(1,n-1):
    ans=max(ans,d1[i-1]+d2[i+1])

print(ans)