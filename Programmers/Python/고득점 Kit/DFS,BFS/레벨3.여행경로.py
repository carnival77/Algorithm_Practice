# from collections import deque


# 넓이우선탐색인 bfs는 연결된 노드를 한 번에 모두 방문하므로 안 된다.
# 깊이우선탐색인 dfs를 써야 한다.
answer = []

# def bfs(g,d,start,visited):
#     global answer
#
#     q=deque()
#     q.append(start)
#     # visited[start]=True
#
#     # reversed_d = {v: k for k, v in d.items()}  # // {'AA': '0', 'BB': '1', 'CC': '2'}
#
#     start_point = [k for k, v in d.items() if v == start]
#
#     answer.append(start_point[0])
#
#     while q:
#         fr=q.popleft()
#
#         candidates_inx = g[fr]
#         candidates=[]
#
#         for candidate_inx in candidates_inx:
#             candidate = [k for k, v in d.items() if v == candidate_inx]
#             candidates.append(candidate[0])
#
#         candidates.sort()
#
#         for to in candidates:
#             print("from : ",fr,"to : ",to)
#
#             q.append(d[to])
#             answer.append(to)
#             g[fr].remove(d[to])
#
#         # for to in g[fr]:
#         #     q.append(to)
#         #     point = [k for k, v in d.items() if v == to]
#         #     answer.append(point[0])
#         #     g[fr].remove(to)

# def dfs(g,d,fr,n):
#     global answer
#
#     # visited[start]=True
#
#     # reversed_d = {v: k for k, v in d.items()}  # // {'AA': '0', 'BB': '1', 'CC': '2'}
#
#     print()
#
#     fr_point = [k for k, v in d.items() if v == fr]
#
#     print(fr_point[0])
#
#     answer.append(fr_point[0])
#
#     print("answer :", answer)
#
#     stop=True
#     for row in g:
#         if row != []:
#             stop=False
#
#     if stop:
#         return answer
#
#     # g[fr].remove(d[fr_point[0]])
#
#     candidates = []
#
#     if len(g[fr]) > 1:
#         candidates_inx = g[fr]
#         # candidates=[]
#
#         for candidate_inx in candidates_inx:
#             candidate = [k for k, v in d.items() if v == candidate_inx]
#             candidates.append(candidate[0])
#
#         candidates.sort()
#
#     elif len(g[fr]) == 1:
#         candidate_inx=g[fr][0]
#         candidate = [k for k, v in d.items() if v == candidate_inx]
#         candidates.append(candidate[0])
#
#     else:
#         return
#
#     print(g[fr])
#     print("candidates : ",candidates)
#
#
#     for to in candidates:
#         print("from : ",fr_point[0],"to : ",to)
#
#         # q.append(d[to])
#         # answer.append(to)
#
#         g[fr].remove(d[to])
#         dfs(g,d,d[to],n)
#
#         # for to in g[fr]:
#         #     q.append(to)
#         #     point = [k for k, v in d.items() if v == to]
#         #     answer.append(point[0])
#         #     g[fr].remove(to)


# def solution(tickets):
#     global answer
#
#     n=len(tickets)
#
#     visited=[False] * 10000
#
#     d=dict()
#
#     g=[[] for _ in range(10000)]
#
#     inx=0
#
#     for fr,to in tickets:
#         if fr not in d:
#             d[fr] = inx
#             inx+=1
#         if to not in d:
#             d[to] = inx
#             inx+=1
#
#         fr_inx = d.get(fr)
#         to_inx = d.get(to)
#
#         g[fr_inx].append(to_inx)
#         # g[to_inx].append(fr_inx)
#
#     # bfs(g,d,0,visited)
#     answer = dfs(g,d,0,n)
#
#     return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

# print(solution(tickets))

## solution 3. dfs 의 stack 사용

from collections import defaultdict

def solution(tickets):

    routes = defaultdict(list)

    for fr,to in tickets:
        routes[fr].append(to)

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack=['ICN']
    path=[]

    while stack:
        top = stack[-1]

        if not routes[top]:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())

    path.reverse()

    return path

print(solution(tickets))

# Reference
# https://kyoung-jnn.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-DFS-%EC%8A%A4%ED%83%9D
# https://gurumee92.tistory.com/165
# dd