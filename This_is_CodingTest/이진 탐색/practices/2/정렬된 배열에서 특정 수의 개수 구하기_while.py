import sys
n,x=map(int,input().split())
a=list(map(int,input().split()))
start=0
end=n-1

def bisect_left(start,end):
    while start<=end:
        mid=(start+end)//2
        if a[mid]==x and (mid==0 or a[mid-1]<x):
            return mid
        elif a[mid]>=x:
            end=mid-1
        else:
            start=mid+1
    return None

def bisect_right(start,end):
    while start<=end:
        mid=(start+end)//2
        if a[mid]==x and (mid==n-1 or a[mid+1]>x):
            return mid
        elif a[mid]>x:
            end=mid-1
        else:
            start=mid+1
    return None

first_index = bisect_left(start,end)

if first_index == None:
    print(-1)
    sys.exit(0)

last_index = bisect_right(start,end)

print(last_index - first_index + 1)