import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m,n,x,y = map(int,input().split())

    x-=1
    y-=1

    answer= False

    k=x

    while k < n*m:
        if k%n== y:
            print(k+1)
            answer = True
            break
        k+=m
    if answer == False:
        print(-1)


# t = int(input())
# for _ in range(t):
#     m,n,x,y = map(int,input().split())
#     x -= 1
#     y -= 1
#     k = x
#     while k < n*m:
#         if k%n == y:
#             print(k+1)
#             break
#         k += m
#     else:
#         print(-1)