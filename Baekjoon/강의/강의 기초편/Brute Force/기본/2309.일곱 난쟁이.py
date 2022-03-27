# 9개 중 서로 다른 2개를 찾기 위해 2중 for문을 쓰는데 그 중 내부 for문은 인덱스를 0이 아닌 1부터 시작해서 서로 다른 수를 고르게 하는 것

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