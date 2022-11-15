n,c=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))

a.sort()

start=1
end=a[-1]-a[0]
ans=0

while start<=end:
    mid=(start+end)//2
    installed_point=a[0]
    cnt=1

    for i in range(1,n):
        if a[i]>=installed_point+mid:
            installed_point=a[i]
            cnt+=1

    if cnt<c:
        end=mid-1
    else:
        start=mid+1
        ans=mid

print(ans)