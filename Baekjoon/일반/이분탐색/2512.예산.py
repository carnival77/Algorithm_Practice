n=int(input())
a=list(map(int,input().split()))
m=int(input())
ans=0
a.sort()

start=0
end=max(a)
while start<=end:
    total=0
    mid = (start + end) // 2
    for x in a:
        if x<mid:
            total+=x
        else:
            total+=mid
    if total>m:
        end=mid-1
    else:
        start=mid+1
        ans=mid

print(ans)