from itertools import combinations

# solutio 1 : combinations 사용
def solution(line):
    answer = []

    INF = float('inf')

    intersections=[]

    max_x=-INF
    min_x=INF
    max_y=-INF
    min_y=INF

    for first,second in combinations(line,2):
        a,b,e = first
        c,d,f = second

        mod = (a*d - b*c)
        if mod==0:
            continue

        x = (b * f - e * d) / mod
        y = (e * c - a * f) / mod

        if x!=int(x) or y!=int(y):
            continue
        x=int(x)
        y=int(y)

        intersections.append((x,y))

        max_x = max(x, max_x)
        min_x = min(x, min_x)
        max_y = max(y, max_y)
        min_y = min(y, min_y)

    h=max_y-min_y+1
    w=max_x-min_x+1

    matrix = [['.'] * w for _ in range(h)]

    for x,y in intersections:
        matrix[max_y-y][x-min_x] = '*'

    for i in range(h):
        answer.append("".join(matrix[i]))

    return answer

# solution 2 : 2중 for문 사용
def solution2(line):
    INF = float('inf')
    mark,L = [],len(line)
    minx,maxx,miny,maxy=INF,-INF,INF,-INF
    for i in range(L):
        for j in range(i,L):
            if i==j : continue
            A,B,E,C,D,F = *line[i],*line[j]
            mo = A*D-B*C
            if mo==0: continue
            x,y=(B*F-E*D)/mo,(E*C-A*F)/mo
            if x-int(x) or y-int(y) : continue
            x,y=int(x),int(y)
            minx,maxx,miny,maxy = min(minx,x),max(maxx,x),min(miny,y),max(maxy,y)
            mark.append((x,y))
    res=[['.' for _ in range(maxx-minx+1)] for _ in range(maxy-miny+1)]
    for x,y in mark : res[maxy-y][x-minx] = '*'
    return [''.join(s) for s in res]

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))