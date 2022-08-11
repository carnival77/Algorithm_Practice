#!/usr/bin/env Python
# coding=utf-8

# 1st try. bfs. 하지만, n이 10억 이하의 자연수이기에, bfs로 모든 경우의 수를 탐색할 수 없다.
# from collections import deque

# def solution(n):
#     ans = 0
    # MAX=2*(n+1)
    # MAX=n+1

    # q=deque()
    # dist=list(i for i in range(MAX+1))
    # check=[False]*MAX
    # dist[0]=0
    # check[0]=True
    # q.append(0)
    # k=1
    #
    # while q:
    #     now=q.popleft()
    #     if now>n:
    #         break
    #     # if now + 1<=MAX and not check[now + 1]:
    #     next=now+1
    #     if next<=MAX and dist[next]>=dist[now]+1:
    #         dist[next]=min(dist[next],dist[now]+1)
    #         # check[now + 1]=True
    #         q.append(next)
    #     next = now*2
    #     if next<=MAX and dist[next]>=dist[now]:
    #         dist[next]=min(dist[next],dist[now])
    #         # check[now*2]=True
    #         q.append(next)
    #
    # ans=dist[n]

    # return ans

# 2nd try. dp. 하지만 효율성에서 탈락.
# def solution(n):
#     ans = 0
#     d = list(i for i in range(n+1))
#     for i in range(2, n + 1):
#         if d[i]>d[i - 1] + 1:
#             d[i]=d[i-1]+1
#         if i % 2 == 0 and d[i] > d[i // 2]:
#             d[i] = d[i // 2]
#     return d[n]

def solution(n):
    ans = 1

    while n!=1:
        if n%2==0:
            n//=2
        else:
            n-=1
            ans+=1

    return ans

N=5000
print(solution(N))