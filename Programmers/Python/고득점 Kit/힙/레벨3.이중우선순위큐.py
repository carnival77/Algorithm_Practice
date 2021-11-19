# 배운 점 :
# 1. heapq.nlargest(n, list) 함수
# heap q list에서 가장 큰 n개의 수의 리스트를 뽑아낼 수 있다.
# 2. heapq.snmallest(n,list) 함수
# heap q list 에서 가장 작은 수 n개의 리스트를 뽑는다.

import heapq

# solution 1 : nlargest, nsmallest 함수 사용
def solution(operations):
    answer = []

    q=[]

    for op in operations:
        cmd,num = op.split()
        num=int(num)
        if cmd=="I":
            heapq.heappush(q,num)
        elif cmd=="D" and q:
            if num==-1:
                heapq.heappop(q)
            else:
                max_val=heapq.nlargest(1,q)[0]
                q.remove(max_val)
                heapq.heapify(q)

    if q:
        answer=[heapq.nlargest(1,q)[0],heapq.nsmallest(1,q)[0]]
    else:
        answer=[0,0]


    return answer


# solution 2 : max_q,min_q 나눠서 사용
def solution2(operations):
    answer=[]

    min_q=[]
    max_q=[]

    for op in operations:
        cmd,num = op.split()
        num=int(num)
        if cmd=="I":
            heapq.heappush(min_q,num)
            heapq.heappush(max_q,(-num,num))
        elif cmd=="D" and min_q and max_q:
            if num==-1:
                val = heapq.heappop(min_q)
                max_q.remove((-val,val))
            else:
                val = heapq.heappop(max_q)[1]
                min_q.remove(val)

    if min_q and max_q:
        answer=[heapq.heappop(max_q)[1],heapq.heappop(min_q)]
    else:
        answer=[0,0]

    return answer

operations=	["I 7","I 5","I -5","D -1"]
print(solution(operations))