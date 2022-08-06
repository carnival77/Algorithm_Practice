import sys
n=int(input())
a=list(map(int,input().split()))
res=sys.maxsize
ans=[]
a.sort()

for i in range(n-2):
    for j in range(i+1,n-1):
        cur1=a[i]
        cur2=a[j]
        cur=cur1+cur2

        start=j+1
        end=n-1

        while start<=end:
            mid=(start+end)//2
            s=cur+a[mid]

            if abs(s)<res:
                res=abs(s)
                ans=[cur1,cur2,a[mid]]
                if res==0:
                    break
                    print(" ".join(map(str,ans)))
                    sys.exit(0)

            if s<0:
                start=mid+1
            else:
                end=mid-1

print(" ".join(map(str,ans)))