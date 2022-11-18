n=int(input())
m=int(input())
a=list(map(int,input().split()))

a.sort()
left_index=0
right_index=n-1
ans=0

while left_index<right_index:
    s=a[left_index]+a[right_index]
    if s==m:
        ans+=1
        left_index+=1
        right_index-=1
    elif s<m:
        left_index+=1
    else:
        right_index-=1

print(ans)