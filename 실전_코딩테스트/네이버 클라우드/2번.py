answer = 0

def recur(costs,x,y,profits,xcost,ycost,n,m, total_sum):
# def recur(costs,x,y,profits,xcost,ycost,answer,n,m):
    global answer

    if profits > answer:
        # print("profits : ",profits)
        # print("answer 1 : ",answer)
        # answer=max(answer,profits)
        answer = profits
        print("answer 2 : ",answer)
        print()
        # return answer
    # else:
    # print("check else")

    if ycost>total_sum:
        pass
    else:
        ny = y+1
        if ny<n:
            y=ny
            # print("check 1 : y,x : ", y,x)
            # print("costs[y][x] : ", costs[y][x])
            profits += costs[y][x]
            profits -= ycost
            print("y축 profits : ", profits)
            print("check 2 : y,x : ", y,x)
            recur(costs, x, y, profits, xcost, ycost, n, m, total_sum)
            # answer = max(answer, recur(costs, x, y, profits, xcost, ycost, n, m))
            # recur(costs,x,y,profits,xcost,ycost,answer,n,m)

    if xcost>total_sum:
        pass
    else:
        nx = x+1
        if nx < m:
            x=nx
            # print("costs[y][x] : ", costs[y][x])
            profits+= costs[y][x]
            profits-= xcost
            print("x축 profits : ",profits)
            print("check 1 : y,x : ",y,x)
            recur(costs, x, y, profits, xcost, ycost, n, m, total_sum)
            # answer = max(answer,recur(costs, x, y, profits, xcost, ycost, n, m))
            # recur(costs,x,y,profits,xcost,ycost,answer,n,m)

def solution(costs,xcost,ycost):
    global answer
    x,y=0,0
    profits=costs[x][y]
    answer=profits
    n=len(costs)
    m=len(costs[0])
    # result=recur(costs,x,y,profits,xcost,ycost,answer,n,m)
    total_sum = 0
    for row in costs:
        total_sum+=sum(row)

    print("answer : ",answer)
    recur(costs, x, y, profits, xcost, ycost, n, m, total_sum)
    # print("result : ",result)

    return answer

costs = [[1,2,3],[4,5,6],[7,8,9]]
xcost=100
ycost=0

print(solution(costs,xcost,ycost))