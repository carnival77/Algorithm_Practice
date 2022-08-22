import heapq,sys

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)] # 강의 리스트
b=[] # 가장 빨리 끝나는 강의 시간 우선순위 큐. 아래 프로세스를 통해, 각 강의의 종료 시간들이 최종적으로 남는다.
heapq.heapify(a)
if n==1:
    ans=1
    print(ans)
    sys.exit(0)
else:
    s,t=heapq.heappop(a)
    heapq.heappush(b,t)#시작시간이 가장 빠른 강의의 종료시간을 heapq에 넣어줌
while len(a)!=0:#모든 강의를 처리할때까지
    s,t=heapq.heappop(a) # 이번 강의 시작, 종료 시간
    x=heapq.heappop(b) # 가장 빨리 끝나는 강의의 종료 시간
    if s<x: # 가장 빨리 수업이 끝나는 강의보다 이번 강의 시작 시간이 작으면(이르면)
        heapq.heappush(b,x) # 가장 빨리 끝나는 강의가 아직 끝나지 않았으므로 가장 빨리 끝나는 강의의 종료 시간을 도로 넣는다.
    heapq.heappush(b,t) # 가장 빨리 수업이 끝나는 강의보다 이번 강의 시작 시간이 같거나 크면(늦으면), 가장 빨리 끝나는 강의가 끝났으므로 가장 빨리 끝나는 강의의 종료 시간을 도로 넣지 않는다.
    # 또한 이번 강의의 종료 시간을 가장 빨리 끝나는 강의 시간 우선순위 큐에 넣는다.
ans=len(b) # 각기 다른 강의실 종료 시간의 개수 = 강의 총 개수
print(ans)
# 참고 자료 : https://yuna0125.tistory.com/45?category=1261068