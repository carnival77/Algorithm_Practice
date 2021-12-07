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
    global temp, visited,matrix,result
    answer = 0

    matrix=computers

    result = [-1] * n
    visited = [False] * n

    for i in range(n):
        bfs(i,n)

    # print(result)

    return len(set(result))

n=3
computers = 	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = 		[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n,computers))