def process(n,m,a):
    # 4칸 같은 게 있는 지 체크
    c=[[False]*m for _ in range(n)]

    # 같은 게 있으면 True
    ok=False

    # board 탐색 - 같은 4개 찾기
    for x in range(n-1):
        for y in range(m-1):
            if a[x][y]!="a" and a[x][y] == a[x+1][y] == a[x][y+1] == a[x+1][y+1]:
                c[x][y] = c[x+1][y] = c[x][y+1] = c[x+1][y+1]=True
                ok=True

    return ok,c

def solution(m, n, board):
    n,m=m,n
    answer = 0

    a=[[0] * m for _ in range(n)]
    for i in range(len(board)):
        a[i]=list(board[i])

    while True:
        ok,c = process(n,m,a)
        # 같은 게 없다면 break
        if not ok:
            break

        # c에서 True 인 같은 것들 없애기(a로 변환)
        for x in range(n):
            for y in range(m):
                if c[x][y]:
                    a[x][y] = "a"
                    # 같은 블록의 개수 answer에 더하기
                    answer+=1


        # board 에서 'a'인 칸들 무시하고 블럭 떨어뜨리기
        cnt = 1
        while cnt: # 움직이는 대상이 더 없어 0이 될 때까지
            cnt=0 # 움직이는 대상의 수
            for x in range(n-1):
                for y in range(m):
                    if a[x][y]!="a" and a[x+1][y]=="a":
                        a[x][y],a[x+1][y] = a[x+1][y],a[x][y]
                        cnt+=1

    return answer

# m=4
# n=5
# board=["CCBDE", "AAADE", "AAABF", "CCBBF"]
m=6
n=6
board = 	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m,n,board))

