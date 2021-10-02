# 1. 특정한 조건이 있는 경우를 모두 통합해서 after라는 한 배열에 넣고 처리한다.
# 2. 결국 x -> y로 이동하는 것이란 걸 기억하자.


from collections import deque

MAX=101

n,m = map(int,input().split())
after=[-1]*101
dist = [-1]*101
for  _ in range(n+m):
    x,y = map(int,input().split())
    after[x] = y
dist[1] = 0
q=deque()
q.append(1)
while q:
    x=q.popleft()
    for i in range(1,7):
        y=x+i
        if y>100: continue
        # 만약 특정 사다리나 뱀을 처음 이용하는 경우라면
        if after[y] != -1 and dist[after[y]] == -1:
            # 사다리, 뱀을 이용하는 경우의 거리와
            dist[after[y]] = dist[x] + 1
            # 이용하지 않는 경우를 모두 넣는다.
            dist[y] = dist[x]+1
            q.append(after[y])
        # 사다리나 뱀을 이용 안 하는 경우
        else:
            if after[y] == -1 and dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)
print(dist[100])


# check=[False]*MAX
# dist=[0]*MAX
# lad=[]
# snake=[]
#
# n,m = map(int,input().split())
#
# for i in range(n):
#     start,end = map(int,input().split())
#     lad.append((start,end))
#
# for i in range(m):
#     start,end = map(int,input().split())
#     snake.append((start,end))
#
# q=deque()
# q.append(1)
#
# while(q):
#     now=q.popleft()
#     for start,end in lad:
#         if now==start : now = end
#     for start,end in snake:
#         if now==start : now = end
#     if (now+1) < MAX:
#         next = now+1
#         if check[next] == False:
#             check[next] = True
#             dist[next] = dist[now] + 1
#             q.append(next)
#     if (now+2) < MAX:
#         next = now+2
#         if check[next] == False:
#             check[next] = True
#             dist[next] = dist[now] + 1
#             q.append(next)
#     if (now+3) < MAX:
#         next = now+3
#         if check[next] == False:
#             check[next] = True
#             dist[next] = dist[now] + 1
#             q.append(next)
#     if (now+4) < MAX:
#         next = now+4
#         if check[next] == False:
#             check[next] = True
#             dist[next] = dist[now] + 1
#             q.append(next)
#     if (now+5) < MAX:
#         next = now+5
#         if check[next] == False:
#             check[next] = True
#             dist[next] = dist[now] + 1
#             q.append(next)
#     if (now+6) < MAX:
#         next = now+6
#         if check[next] == False:
#             check[next] = True
#             dist[next] = dist[now] + 1
#             q.append(next)
# print(dist)
# print(dist[100])