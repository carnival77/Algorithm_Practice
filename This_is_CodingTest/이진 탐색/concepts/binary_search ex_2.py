def binary_search(arr,tg,start,end):
    while start <= end :
        mid = (start+end)//2
        if arr[mid] == tg:
            return mid
        elif arr[mid]>tg:
           end = mid-1
        else:
            start  = mid + 1
    return None

n, target = list(map(int,input().split()))

arr= list(map(int,input().split()))

result = binary_search(arr,target,0,n-1)
print(result+1)