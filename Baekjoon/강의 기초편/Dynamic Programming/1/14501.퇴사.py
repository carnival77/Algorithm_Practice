# solution1. 브루트 포스
n=int(input())

t=[0]*n
p=[0]*n

for i in range(n):
    t[i],p[i]=map(int,input().split())

max_p=-1

def dfs(index,total_p):
    global t,p,n,max_p

    if index > n:
        return

    if index==n:
        if total_p > max_p:
            max_p = total_p
        return

    if total_p > max_p:
        max_p = total_p

    dfs(index+t[index],total_p+p[index])
    dfs(index+1,total_p)

dfs(0,0)

print(max_p)

# solution 2. 다이나믹 프로그래밍
inf = 10**9
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
d = [-1]*(n+1)
for i in range(1, n+1):
    t[i],p[i] = map(int,input().split())
ans = 0
def go(day):
    if day == n+1:
        return 0
    if day > n+1:
        return -inf
    if d[day] != -1:
        return d[day]
    t1 = go(day+1) # x
    t2 = p[day] + go(day+t[day]) # o
    d[day] = max(t1,t2)
    return d[day]

print(go(1))