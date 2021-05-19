n=int(input())

arr = list(map(int,input().split()))

d=[0]*100

d[0] = arr[0]
d[1]=arr[1]
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+arr[i])

print(d[n-1])



# n=int(input())
#
# arr = list(map(int,input().split()))
#
# d=[0]*101
#
# d[0] = arr[0]
# d[1]=arr[1]
# for i in range(2,n+1):
#     d[i] = max(d[i-1],d[i-2]+arr[i])
#
# print(d[n])