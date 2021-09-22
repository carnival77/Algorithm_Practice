n = int(input())
board=[]

for i in range(n):
    board.append(list(map(int,input())))

index=2
ans=[]
num=0

def dfs(start,index):
    global num
    x,y = start

    if x<0 or y<0 or x>n-1 or y>n-1:
        return False
    if board[x][y] == 1:
        board[x][y] = index
        num+=1
        dfs((x+1,y),index)
        dfs((x-1,y),index)
        dfs((x,y-1),index)
        dfs((x,y+1),index)
        return True

    return False

total=0

for i in range(n):
    for j in range(n):
        if(board[i][j] == 1):
            if(dfs((i,j),index)):
                total+=1
            index+=1
            ans.append(num)
            num=0

print(total)
ans.sort()
for i in ans:
    print(i)