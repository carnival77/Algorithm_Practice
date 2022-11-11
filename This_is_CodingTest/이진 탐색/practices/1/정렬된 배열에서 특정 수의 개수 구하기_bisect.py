from bisect import bisect_left, bisect_right

import sys

n,x = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

def count_element(arr,left_value,right_value):
    right_index = bisect_right(arr,right_value)
    left_index = bisect_left(arr,left_value)
    return right_index-left_index

if count_element(arr,x,x) != 0:
    print(count_element(arr,x,x))
else:
    print(-1)


