a=[]

def process(x1,y1,x2,y2):
    global a

    #rotate
    tmp=a[x1][y1]
    nums=[tmp]

    for i in range(x1,x2):
        a[i][y1]=a[i+1][y1]
        nums.append(a[i+1][y1])

    for i in range(y1,y2):
        a[x2][i]=a[x2][i+1]
        nums.append(a[x2][i+1])

    for i in range(x2,x1,-1):
        a[i][y2]=a[i-1][y2]
        nums.append(a[i-1][y2])

    for i in range(y2,y1,-1):
        a[x1][i]=a[x1][i-1]
        nums.append(a[x1][i-1])

    a[x1][y1+1]=tmp

    return min(nums)


def solution(rows, columns, queries):
    global a
    answer = []

    a=[[0]*columns for i in range(rows)]

    cnt=1

    for i in range(rows):
        for j in range(columns):
            a[i][j]=cnt
            cnt+=1

    for query in queries:
        x1,y1,x2,y2=query
        x1-=1
        y1-=1
        x2-=1
        y2-=1

        answer.append(process(x1,y1,x2,y2))

    return answer

# solution 2. stack 활용
def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1


        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]


        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))


    return answer

# solution 3. map, zip 활용
def solution(rows, columns, queries):
    matrix = [list(range(r * columns +1,r * columns + columns +1))for r in range(rows)]

    ans = []
    for x1,y1,x2,y2 in queries:
        arr = matrix[x1 - 1][y1-1:y2]+ [matrix[i][y2-1]for i in range(x1-1,x2)][1:-1] + matrix[x2 - 1][y1-1:y2][::-1] + [matrix[i][y1-1]for i in range(x1-1,x2)][::-1][1:-1]
        ans.append(min(arr))

        arr = [arr[-1]] + arr[:-1]
        a,b,c,d = arr[:y2-y1+1],arr[y2-y1+1: y2-y1 + x2-x1 ],arr[y2-y1+x2-x1:y2-y1+x2-x1+y2-y1+1],arr[y2-y1+x2-x1+y2-y1+1:]
        matrix[x1 - 1][y1-1:y2] = a
        matrix[x2 - 1][y1-1:y2] = c[::-1]

        matrix = list(map(list,zip(*matrix)))
        matrix[y2-1][x1:x2-1] = b
        matrix[y1-1][x1:x2-1] = d[::-1]
        matrix = list(map(list,zip(*matrix)))
    return ans

# solution 4. deque 활용
from collections import deque
def solution(rows, columns, queries):
    arr = [[i+columns*j for i in range(1,columns+1)] for j in range(rows)]
    answer, result = deque(), []
    for i in queries:
        a,b,c,d = i[0]-1,i[1]-1,i[2]-1,i[3]-1
        for x in range(d-b):
            answer.append(arr[a][b+x])
        for y in range(c-a):
            answer.append(arr[a+y][d])
        for z in range(d-b):
            answer.append(arr[c][d-z])
        for k in range(c-a):
            answer.append(arr[c-k][b])
        answer.rotate(1)
        result.append(min(answer))
        for x in range(d-b):
            arr[a][b+x] = answer[0]
            answer.popleft()
        for y in range(c-a):
            arr[a+y][d] = answer[0]
            answer.popleft()
        for z in range(d-b):
            arr[c][d-z] = answer[0]
            answer.popleft()
        for k in range(c-a):
            arr[c-k][b] = answer[0]
            answer.popleft()
    return result