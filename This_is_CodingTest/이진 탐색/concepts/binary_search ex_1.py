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

n, target = list(map(int,input().split()))

arr= list(map(int,input().split()))

result = binary_search(arr,target,0,n-1)
print(result+1)