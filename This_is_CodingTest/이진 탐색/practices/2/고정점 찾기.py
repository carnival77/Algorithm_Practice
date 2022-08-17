n=int(input())
a=list(map(int,input().split()))

start=0
end=n-1

def bs(start,end):
    while start<=end:
        mid=(start+end)//2
        tg=a[mid]
        if tg==mid:
            return mid
        elif tg<mid:
            start=mid+1
        else:
            end=mid-1

    return -1

print(bs(start,end))