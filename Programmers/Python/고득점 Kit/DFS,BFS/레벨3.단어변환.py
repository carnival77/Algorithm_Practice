import sys
from collections import deque

# 서로 한 개의 알파벳만 다른 단어(노드)끼리 연결지어 그래프 생성.
def makeGraph(dic,n):
    graph=[[] for _ in range(n)]

    for i in range(n-1):
        word=dic[i]
        for j in range(i+1,n):
            target=dic[j]

            cnt=0
            for x,y in zip(word,target):
                if x!=y:
                    cnt+=1

            if cnt == 1:
                graph[i].append(j)
                graph[j].append(i)

    return graph

def solution(begin, target, words):
    answer = 0

    n=len(words)+1
    visited=[False]*n
    dist=[0]*n

    dic={0:begin}

    for i,word in enumerate(words):
        dic[i+1]=word

    graph = makeGraph(dic,n)

    # print(graph)

    q=deque()
    q.append(0)

    visited[0]=True

    target_inx=0

    for key, value in dic.items():
        if value == target:
            target_inx = key

    while q:
        x = q.popleft()

        for y in graph[x]:
            if visited[y]==False:
                visited[y]=True
                q.append(y)
                dist[y]=dist[x]+1

                if y == target_inx:
                    return dist[y]

    return 0