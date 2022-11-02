import heapq

n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
ans=0
heapq.heapify(a)

while True:
    if len(a)>=2:
        x=heapq.heappop(a)
        y=heapq.heappop(a)
        ans+=(x+y)
        heapq.heappush(a,x+y)
    else:
        break

print(ans)