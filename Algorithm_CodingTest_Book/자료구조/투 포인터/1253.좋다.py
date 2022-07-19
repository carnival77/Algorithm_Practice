from collections import defaultdict

n=int(input())
a=list(map(int,input().split()))

a.sort()
ans=0
d=defaultdict(int)

for i in range(n):
    left_index = 0
    right_index = n - 1
    while left_index<right_index:
        if left_index==i:
            left_index+=1
        elif right_index==i:
            right_index-=1
        if left_index==right_index:
            break
        s=a[left_index]+a[right_index]
        if s==a[i]:
            d[a[i]]+=1
            left_index+=1
            right_index-=1
            break
        elif s<a[i]:
            left_index+=1
        else:
            right_index-=1
ans=sum(d.values())
print(ans)

# 반례
# 3
# 0 0 1
# 정답: 0