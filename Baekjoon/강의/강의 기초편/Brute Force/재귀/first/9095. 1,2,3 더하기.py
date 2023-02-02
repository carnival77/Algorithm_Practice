from itertools import product

t = int(input())

def dfs(sum,cnt,n):
    if sum==n:
        return 1
    if sum>n:
        return 0
    answer = 0
    for i in range(1,4):
        answer += dfs(sum+i,cnt+1,n)

    return answer

for i in range(t):
    print(dfs(0,0,int(input())))
