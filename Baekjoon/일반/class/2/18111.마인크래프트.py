# # solution 1. 본문대로 구현. 하지만 시간 초과. 시간 제한이 1초이므로, 소요되는 전체적인 시간을 합해보면 많다.
#
# n,m,b=map(int,input().split())
#
# data=[list(map(int,input().split())) for _ in range(n)]
# ans = 0
# s = 0
# cnt=0
# for i in range(n):
#     for j in range(m):
#         s+= data[i][j]
#         cnt+=1
# t = round(s / cnt)
# a=[item[:] for item in data]
# while t>=0:
#     ok=True
#     for i in range(n):
#         for j in range(m):
#             if a[i][j]!=t:
#                 ok=False
#     if ok:
#         break
#     # a=deepcopy(data)
#     a=[item[:] for item in data]
#     c=b
#     # need=0
#     time = 0
#     next=False
#     for i in range(n):
#         for j in range(m):
#             if a[i][j]==t:
#                 continue
#             elif a[i][j]<t: # 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.
#                 if c>=1:
#                     c-=1
#                     a[i][j]+=1
#                     time+=1
#                 # dif=t-a[i][j]
#                 # if c>=dif:
#                 #     a[i][j]+=dif
#                 #     c-=dif
#                 #     time+=dif
#                 else:
#                     next=True
#                     t-=1
#                     break
#                 # need+=dif
#             else: # a[i][j]>t # 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
#                 a[i][j]-=1
#                 c+=1
#                 time+=2
#                 # dif=a[i][j]-t
#                 # a[i][j]-=dif
#                 # c+=dif
#                 # time+=2*dif
#         if next:
#             break
# ans=time
# print(ans,t)

# solution 2.
# 추가시간이 주어지지 않으므로 도중에 검사하기보다 모든 원소를 돌고나서 체크를 하는것이 낫다.
# 인벤토리로 들어가는 블록의 갯수와 초기 인벤토리를 합한 것이 인벤토리에서 나가는 블록의 갯수보다 크거나 같다면 그 목표높이로 땅을 고를 수 있다
# 코드에서는 3중 for문을 돌지만 실제로는 최대 높이가 257개(0 포함), 행렬의 최대 사이즈는 250,000이므로 256 * 250,000 = 64,250,000 이므로 충분히 1초만에 모든 경우를 계산할 수 있다.
n,m,b=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=1e9
height=0

for h in range(257):
    remove=0
    install=0
    for i in range(n):
        for j in range(m):
            dif = a[i][j] - h
            if dif==0:
                continue
            elif dif>0:
                remove+=dif
            else:
                install+=abs(dif)
    inventory=b+remove
    if install>inventory:
        continue
    time=2*remove+install
    if time<=ans:
        ans=time
        height=h

print(ans,height)