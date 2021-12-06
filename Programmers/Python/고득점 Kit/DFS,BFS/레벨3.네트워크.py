from collections import deque

temp=[]
matrix=[]
visited=[]

def bfs(s,n):
    q=deque()
    q.append(s)
    visited[s] = True

    while q:
        v=q.popleft()
        for i in range(n):
            if visited[i] == False and matrix[s][i] == 1:
                visited[i]=True
                q.append(i)
                temp[s][i] = s

def solution(n, computers):
    global temp, visited,matrix
    answer = 0

    matrix=computers

    visited = [False] * n
    temp = [[100] * n for _ in range(n)]

    for i in range(n):
        bfs(i,n)

    for i in range(n):
        print(temp[i])

    return answer