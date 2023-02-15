n = int(input())
a = [0] + [int(input()) for _ in range(n)]
d = [0] * (n+1) # d[i] : a[i]까지 마실 수 있는 포도주의 최대치
# a[i]를
# 1) 0번째로 연속해서 마신다면, a[i]를 마시지 않는다
# -> d[i-1]
# 2) 1번째로 연속해서 마신다면, a[i-1]를 마시지 않고, a[i]를 마신다.
# -> d[i-2]+a[i]
# 3) 2번째로 연속해서 마신다면, a[i-2]를 마시지 않고, a[i-1],a[i]를 마신다.
# -> d[i-3]+a[i-1]+a[i]
# 따라서, d[i]=max(d[i-1],d[i-2]+a[i],d[i-3]+a[i-1]+a[i])
d[1] = a[1]
if n >= 2:
    d[2] = a[1]+a[2]
for i in range(3,n+1):
    d[i]=max(d[i-1],d[i-2]+a[i],d[i-3]+a[i-1]+a[i])
print(d[n])