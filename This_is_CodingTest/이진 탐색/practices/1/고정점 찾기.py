import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

start = 0
end = n-1

answer = 0

count = 0

i=0

while start<=end:

    mid = (start+end) // 2

    target = arr[i]

    if mid == arr[mid]:
        answer = mid
        count += 1
        break
    elif arr[mid] < mid:
        start = mid+1
    else:
        end = mid-1

    i += 1

if count == 1:
    print(answer)
else:
    print(-1)