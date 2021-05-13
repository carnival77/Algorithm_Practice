def binary_search(arr,tg,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    if arr[mid] == tg:
        return mid
    elif arr[mid]>tg:
        return binary_search(arr,tg,start,mid-1)
    else:
        return binary_search(arr,tg,mid+1,end)

n = int(input())
arr = list(map(int,input().split()))

m = int(input())
x= list(map(int,input().split()))

for i in x:
    result = binary_search(arr,i,0,n-1)
    if result !=None:
        print("yes")
    else:
        print("no")
