n,m=map(int,input().split())
a=list(map(int,input().split()))

left_index=0
right_index=0
ans=0
s=0

while right_index<n:
    s=sum(a[left_index:right_index+1])
    if s==m:
        ans+=1
        right_index+=1
    elif s>m:
        left_index+=1
    else:
        right_index+=1

print(ans)