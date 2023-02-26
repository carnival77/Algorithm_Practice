import heapq,sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    k=int(input())
    answer = []

    min_q = []
    max_q = []
    need=[False]*1000001 # 최소, 최대 우선순위 큐 모두에서 공통으로 존재하기에 삭제 대상이 아닌 것(True)과, 한 쪽에서는 존재하지 않아 삭제 대상인 것(False).

    for index in range(k):
        cmd, num = map(str,input().split())
        num = int(num)
        if cmd == "I":
            heapq.heappush(min_q, (num,index))
            heapq.heappush(max_q, (-num,index))
            need[index]=True # 두 큐에서 공통으로 존재하기에 삭제 대상이 아님.
        # 삭제 연산 시,
        elif cmd == "D":
            if num == -1:
                # index값을 기준으로 need 리스트에서 해당 노드가 다른 큐에서 삭제된 노드인 지 확인하고
                # 삭제된 노드들은 큐에서 삭제하는 것을 삭제 대상 노드가 나올 때까지 반복하고,
                while min_q and not need[min_q[0][1]]:
                    heapq.heappop(min_q)
                # 삭제 대상 노드가 나오면 삭제
                if min_q:
                    val,index = heapq.heappop(min_q)
                    need[index]=False # 삭제된 노드의 인덱스로 해당 노드를 삭제 대상으로 변경
            else:
                while max_q and not need[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    val,index=heapq.heappop(max_q)
                    need[index]=False

    # 모든 삽입, 삭제 질의 수행 후, need 리스트에서 삭제 대상인 노드는 모두 필요하지 않으므로 삭제한다.
    while max_q and not need[max_q[0][1]]:
        heapq.heappop(max_q)
    while min_q and not need[min_q[0][1]]:
        heapq.heappop(min_q)

    if min_q and max_q:
        answer = [heapq.heappop(max_q)[0]*-1, heapq.heappop(min_q)[0]]
        print(*answer)
    else:
        print('EMPTY')

# 참고 :
# https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj7662/
# https://esoongan.tistory.com/71