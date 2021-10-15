# solution 2. 인접 행렬, dfs 활용
cnt = 0


def dfs(matrix, V, n, visited):
    global cnt
    visited[V] = True
    cnt += 1

    for i in range(1, n + 1):
        if visited[i] == False and matrix[V][i] == True:
            dfs(matrix, i, n, visited)

    return


def solution(n, wires):
    global cnt
    answer = n
    visited = [False] * (n + 1)

    matrix = [[False] * (n + 1) for _ in range(n + 1)]

    for wire in wires:
        a, b = wire
        matrix[a][b] = matrix[b][a] = True

    for wire in wires:
        a, b = wire
        matrix[a][b] = matrix[b][a] = False
        dfs(matrix, 1, n, visited)

        answer = min(answer, abs(n - 2 * cnt))

        cnt = 0
        visited = [False] * (n + 1)
        matrix[a][b] = matrix[b][a] = True

    return answer

# # solution 1. 유니온 파인드 문제 해결 시도. 그러나 정확도 15퍼. 아래의 유니온 파인드 정답을 보고 수정 요망
# from itertools import combinations
# from collections import Counter

# def find_parent(parent,x):
#     if parent[x] == x:
#         return x
#     parent[x] = find_parent(parent,parent[x])
#     return parent[x]

# def union_parent(parent,a,b):
#     a=find_parent(parent,a)
#     b=find_parent(parent,b)

#     if a<b:
#         parent[b]=a
#     else:
#         parent[a]=b


# def solution(n, wires):
#     answer = n

#     parent = [0] * (n+1)

#     for i in range(n+1):
#         parent[i] = i

#     for wire_combi in combinations(wires,n-2):
#         for wire in wire_combi:
#             a,b = wire
#             union_parent(parent,a,b)
#         cp=Counter(parent[1:])
#         two=[]
#         for i in cp.values():
#             two.append(i)
#         cur = abs(two[0] - two[1])
#         answer=min(answer,cur)
#         for i in range(n+1):
#             parent[i] = i


#     return answer

# uf = []

# def find(a):
#     global uf
#     if uf[a] < 0: return a
#     uf[a] = find(uf[a])
#     return uf[a]

# def merge(a, b):
#     global uf
#     pa = find(a)
#     pb = find(b)
#     if pa == pb: return
#     uf[pa] += uf[pb]
#     uf[pb] = pa

# def solution(n, wires):
#     global uf
#     answer = int(1e9)
#     k = len(wires)
#     for i in range(k):
#         uf = [-1 for _ in range(n+1)]
#         tmp = [wires[x] for x in range(k) if x != i]
#         for a, b in tmp: merge(a, b)
#         v = [x for x in uf[1:] if x < 0]
#         answer = min(answer, abs(v[0]-v[1]))

#     return answer