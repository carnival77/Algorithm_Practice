import sys

n=9
input = sys.stdin.readline
arr = [int(input()) for _ in range(n)]

arr.sort()

total = sum(arr)

for i in range(n):
    for j in range(1,n):
        if total - arr[i]- arr[j] == 100:
            for k in arr:
                if k == arr[i] or k == arr[j]:
                    continue
                else:
                    print(k)
            sys.exit(0)