#solution 1. n이 최대 1천만이므로, 3중 for문을 수행하면 시간 복잡도 초과다.
# def solution(n, left, right):
#     mat = [[0] * n for _ in range(n)]
#
#     for i in range(1, n + 1):
#         for x in range(i):
#             for y in range(i):
#                 if x == i - 1 or y == i - 1:
#                     mat[x][y] = i
#
#     arr = [[0] for _ in range(n * n)]
#
#     for i in range(n):
#         for j in range(n):
#             arr[i * n + j] = mat[i][j]
#
#     return arr[left:right + 1]

#solution 2. 좌표 활용한 공식
def solution(n,left,right):
    arr=[]
    for num in range(left,right+1):
        r,c=divmod(num,n)
        arr.append(max(r,c)+1)

    return arr

n = 3
left = 2
right = 5
print(solution(n, left, right))
