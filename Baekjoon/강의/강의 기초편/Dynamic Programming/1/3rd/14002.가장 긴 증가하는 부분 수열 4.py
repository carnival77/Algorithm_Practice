# n=int(input())
# a=list(map(int,input().split()))
# # d[i] = a[1]...a[i] 까지의 수열이 있을 때, a[i]를 마지막으로 하는 가장 긴 증가하는 부분수열의 길이
# d=[1]*n
# for i in range(n):
#     for j in range(i):
#         # 조건에 맞으려면, a[1] ... a[j],a[i] 수열이 있으면, j<i , a[j] < a[i]. 이어야 한다.
#         # a[j]<a[i] 인 상태에서, d[j] 에 a[i] 1개를 추가한 길이가 d[i]보다 크면, d[i]는 d[j] 에 a[i] 1개를 더한 길이로 변경해준다.
#         if a[i]>a[j] and d[i]<d[j]+1:
#             d[i]=d[j]+1
# max_val=max(d)
# print(max_val)
# ans=[]
# for i in range(n-1,-1,-1):
#     if d[i]==max_val:
#         ans.append(a[i])
#         max_val-=1
# ans.reverse()
# print(" ".join(map(str,ans)))

n=int(input())
a=list(map(int,input().split()))
# d[i] = a[1]...a[i] 까지의 수열이 있을 때, a[i]를 마지막으로 하는 가장 긴 증가하는 부분수열의 길이
d=[1]*n
to=[-1]*n
for i in range(n):
    for j in range(i):
        # 조건에 맞으려면, a[1] ... a[j],a[i] 수열이 있으면, j<i , a[j] < a[i]. 이어야 한다.
        # a[j]<a[i] 인 상태에서, d[j] 에 a[i] 1개를 추가한 길이가 d[i]보다 크면, d[i]는 d[j] 에 a[i] 1개를 더한 길이로 변경해준다.
        if a[i]>a[j] and d[i]<d[j]+1:
            d[i]=d[j]+1
            to[i]=j
ans=[]
def dfs(i):
    global ans
    ans.append(a[i])
    if to[i]!=-1:
        return dfs(to[i])
    else:
        return
target_inx=0
max_d=max(d)
for i in range(n):
    if d[i]==max_d:
        target_inx=i
dfs(target_inx)
ans.reverse()
print(max_d)
print(*ans)