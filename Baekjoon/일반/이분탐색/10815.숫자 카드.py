n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

ans=[]
a.sort()

for target in b:
    start=0
    end=len(a)-1
    ok=0
    while start<=end:
        mid = (start + end) // 2
        if target==a[mid]:
            ok=1
            break
        elif target>a[mid]:
            start=mid+1
        else:
            end=mid-1
    ans.append(ok)

print(" ".join(map(str,ans)))