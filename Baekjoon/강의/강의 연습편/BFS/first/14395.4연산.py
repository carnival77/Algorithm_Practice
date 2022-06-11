# solution
# 정점 = 가능한 수의 개수, 간선 = 4개 연산, 가중치 = 연산 1번 이므로, BFS로 풀이 가능하다.
# 이때, 정점의 개수는 10억(1e9)가 아니다.
# 왜냐하면 4개 연산 중 *,+를 제외한  /,-는 1,0의 결과를 내기 때문에, 결국 가능한 경우의 수는 x^a*2^b의 형태를 띠게 된다.
# 또한 이것의 크기는 사실상 10억을 넘지 않는다.
# 그 이유는 연산 결과가 t보다 큰 경우는, 더 적은 수로 되돌아가는 방법이 /,- 뿐인데, 이것의 결과는 앞서 말했듯 1,0 으로 고정되어 있기에, 최소횟수를 구하는 솔루션 과정에서 굳이 정점의 개수에 더할 필요가 없다.
# x^a*2^b의 형태에서 가능한 a,b의 경우의 수는 b<=30, a<= 약 30 이므로, 가능한 모든 경우의 수는 900개로 정점의 수 또한 약 900개 이하이다.
# 정점의 개수를 N이라 가정했을 때, BFS의 시간 복잡도는, 방문 체크를 하며 모든 정점을 방문하는 시간 + 모든 간선을 확인하는 시간이다.
# 즉, 정점의 개수는 N개이고, 각 정점에서 연결된 간선(연산)은 4개씩이므로 간선의 개수는 4*N개이다. 따라서 총 시간 복잡도는 O(4*N)=O(N)이고, N<=900이므로 BFS로 풀이 가능하다.
# 이때 유의해야 할 점이, 10억을 int 형 배열 check 등으로 선언하면, int형은 4바이트이므로 약 40억 바이트, 즉 4GB의 메모리 공간이 필요하다.
# 이렇게 하면 주어진 조건인 512MB 메모리 공간 조건을 초과한다.
# 따라서 방문 여부 check 는 set으로 선언해야 한다.
# 또한, 사전순으로 앞서는 것을 출력해야 하므로, *,+,-,/ 순으로 큐에 삽입될 수 있도록 코딩 시 순서를 맞춘다.

from collections import deque
import sys

s,t=map(int,input().split())

if s==t:
    print(0)
    sys.exit(0)

LIMIT=int(1e9)
check=set()
check.add(s)
q=deque()
q.append((s,''))

while q:
    x,op=q.popleft()
    if x==t:
        print(op)
        sys.exit(0)
    if 0<=x*x<=LIMIT and x*x not in check:
        q.append((x*x,op+'*'))
        check.add(x*x)
    if 0<=x+x<=LIMIT and x+x not in check:
        q.append((x+x,op+'+'))
        check.add(x+x)
    if 0<=x-x<=LIMIT and x-x not in check:
        q.append((x-x,op+'-'))
        check.add(x-x)
    if x!=0 and 0<=x//x<=LIMIT and x//x not in check:
        q.append((x//x,op+'/'))
        check.add(x//x)

print(-1)