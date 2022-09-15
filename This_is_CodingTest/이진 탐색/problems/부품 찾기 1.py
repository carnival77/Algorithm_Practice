# def binary_search(arr,tg,start,end):
#     if start>end:
#         return None
#     mid = (start+end)//2
#     if arr[mid] == tg:
#         return mid
#     elif arr[mid]>tg:
#         return binary_search(arr,tg,start,mid-1)
#     else:
#         return binary_search(arr,tg,mid+1,end)
#
# n = int(input())
# arr = list(map(int,input().split()))
#
# m = int(input())
# x= list(map(int,input().split()))
#
# for i in x:
#     result = binary_search(arr,i,0,n-1)
#     if result !=None:
#         print("yes")
#     else:
#         print("no")

def binary_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if target==arr[mid]:
            return mid
        elif target<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return None

import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m=int(input())
x=list(map(int,input().split()))

for i in x:
    res=binary_search(arr,i,0,n-1)
    if res!=None:
        print('yes',end=' ')
    else:
        print('no',end=' ')