# solution 1 : bfs 사용

from collections import deque

result=[]
matrix=[]
visited=[]

def bfs(s,n):
    global result
    q=deque()
    q.append(s)
    visited[s] = True

    if result[s] == -1:
        result[s]=s

    while q:
        v=q.popleft()
        for i in range(n):
            if visited[i] == False and matrix[v][i] == 1:
                visited[i]=True
                q.append(i)
                result[i] = s

def solution(n, computers):
    global visited,matrix,result

    matrix=computers

    result = [-1] * n
    visited = [False] * n

    for i in range(n):
        bfs(i,n)
        # dfs(i,n)

    # print(result)

    return len(set(result))

# solution 2 : dfs 사용

def dfs(v,n,visit,computers):
    global result
    visit[v] = True

    for i in range(n):
        if visit[i] == False and computers[v][i] == 1:
            dfs(i,n,visit,computers)

def solution2(n,computers):
    answer=0

    visit=[False]*n

    for i in range(n):
        if visit[i] == False:
            dfs(i,n,visit,computers)
            answer+=1

    return answer

n=3
computers = 	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = 		[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n,computers))