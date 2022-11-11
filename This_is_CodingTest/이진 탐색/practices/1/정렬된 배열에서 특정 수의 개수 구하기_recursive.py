import sys

def count_by_value(arr,x):

    n = len(arr)

    first_index = find_first_index(arr,x,0,n-1)

    if first_index == None:
        return -1

    last_index = find_last_index(arr,x,0,n-1)

    return last_index - first_index + 1



def find_first_index(arr,target,start,end):

    if start > end:
        return None

    mid = (start+end)//2

    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if arr[mid] == target and (mid == 0 or target > arr[mid-1]):
        return mid
    # 중간점의 값보다 target 이 작거나 같은 경우 왼쪽 이분 탐색
    elif arr[mid] >= target:
        return find_first_index(arr,target,start,mid-1)
    # 중간점의 값보다 target 이 큰 경우 오른쪽 이분 탐색
    else:
        return find_first_index(arr,target,mid+1,end)

def find_last_index(arr,target,start,end):

    if start > end :
        return None

    mid = (start + end ) // 2

    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if arr[mid] == target and (mid == n-1 or target < arr[mid+1]):
        return mid
    # 중간점의 값보다 target이 작은 경우 왼쪽 이분 탐색
    elif arr[mid] > target:
        return find_last_index(arr,target,start,mid-1)
    # 중간점의 값보다 target 이 크거나 같은 경우 오른쪽 이분 탐색
    else:
        return find_last_index(arr,target,mid+1,end)

n,x = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

result = count_by_value(arr,x)

if result == -1:
    print(-1)
else:
    print(result)