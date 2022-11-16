import sys
n=int(input())
a=list(map(int,input().split()))
res=float("inf")
ans=[]

for i in range(n-1):
    cur=a[i]

    start=i+1
    end=n-1

    while start<=end:
        mid=(start+end)//2
        s=cur+a[mid]

        if abs(s)<res:
            res=abs(s)
            ans=[cur,a[mid]]
            if res==0:
                break
                print(" ".join(map(str,ans)))
                sys.exit(0)

        if s<0:
            start=mid+1
        else:
            end=mid-1

print(" ".join(map(str,ans)))