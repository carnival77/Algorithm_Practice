# 1

win

1 : (2)
2 : (5)
3 : (2)
4 : (2,3)
5 :

lose

1 :
2 : (1,3,4)
3 : (4)
4 :
5 : (2)

# 2

win

1 : (2)
2 : (5)
3 : (2)
4 : (2,3)
5 :

lose

1 :
2 : (1,3,4)
3 : (4)
4 :
5 : (1,2,3,4)

1,3,4 > 2 , 2 > 5 => 1,3,4 > 5

# solution 1. graph 와 defaultdict(set) 이용

from collections import defaultdict

def solution(n, results):
    answer = 0

    win=defaultdict(set)
    lose=defaultdict(set)

    # 1
    for winner,loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)

    # 2
    for i in range(1,n+1):
        for loser in win[i]:
            lose[loser].update(lose[i]) # i한테 진 애들은 i를 이긴 애들한테도 진 것
        for winner in lose[i]:
            win[winner].update(win[i]) # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것

    for i in range(1,n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer+=1

    return answer

# 참고 : https://velog.io/@narastro/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-Python

# solution 2. 플로이드 워셜 알고리즘

def solution2(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)]
    for win, lose in results:
        matrix[win - 1][lose - 1] = True
        matrix[lose - 1][win - 1] = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[j][i] == None:
                    continue

                if matrix[j][i] == matrix[i][k]:
                    matrix[j][k] = matrix[j][i]
                    matrix[k][j] = not matrix[j][i]

    answer = 0
    for i in range(n):
        if None in matrix[i][:i] + matrix[i][i + 1:]:
            continue
        answer += 1
    return answer

# 참고 : https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B7%B8%EB%9E%98%ED%94%84-Floyd-Warshall-Level3

# 시간복잡도상으로는 1이 더 우수