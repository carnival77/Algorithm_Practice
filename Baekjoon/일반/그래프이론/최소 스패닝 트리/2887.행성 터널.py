v=int(input())
parents=[0]*(v+1)
edges=[]
ans=0

for i in range(1,v+1):
    parents[i]=i

edges=[]

# first try : 메모리/시간 초과
# n 이 100000 일 때
# edges 안에 들어가는 원소의 개수는 10C2 = 100000 * 99999 / 2 = 4999950000 개 입니다.
# 각 원소는 int 3개 = 12 byte 이므로,
# 필요한 메모리의 양은 4999950000 * 12 = 약 56 TB 으로,
# 문제에서 주어진 제한 128 MB 를 훨씬 초과합니다.
# 또한, 문제의 시간 조건 1초(약 2천만 번 연산) 에도 초과된다.
# 아래의 식의 연산은 O(N^2)이기 때문이다.

# points=[list(map(float,input().split())) for _ in range(v)]
# for i in range(len(points)-1):
#     x1,y1,z1=points[i]
#     for j in range(i,len(points)):
#         x2,y2,z2=points[j]
#         cost=min(abs(x1-x2),abs(y1-y2),abs(z1-z2))
#         edges.append((cost, i, j))

# solution. 문제에서 필요한 간선의 조건을 생각한다.
# 간선은 비용인  min(|xA-xB|, |yA-yB|, |zA-zB|)을 기준으로 오름차순 정렬된 배열에서 (n-1)번째까지만 쓰인다.
# 먼저 각 점마다 번호를 부여한다.
points=[[i]+list(map(int,input().split())) for i in range(v)]

for i in range(1,4):
    # 각 요소별로 오름차순 정렬한다.
    s=sorted(points,key=lambda x:x[i])
    # 필요한 값은 min(|xA-xB|, |yA-yB|, |zA-zB|) 이므로,
    # 각 오름차순 정렬된 배열에서 앞에서부터 두 개 요소씩 짝지어 그 차와 번호를 간선 배열에 넣는다.
    for j in range(v-1):
        edges.append((abs(s[j][i]-s[j+1][i]),s[j][0],s[j+1][0]))

# 각 요소별 두 개 요소씩 짝지어 뺄셈한 결과가 모두 저장되어 있으므로,
# 모든 요소를 오름차순 정렬하여 그 중 인덱스 0 ~ (n-1) 번째 요소 내의 정점들이
# 크루스칼 알고리즘에 의해 서로 연결되도록 한다.
edges.sort()

def find_parent(parents,x):
    if parents[x]!=x:
        parents[x]=find_parent(parents,parents[x])
    return parents[x]

def union_parent(parents,a,b):
    a=find_parent(parents,a)
    b=find_parent(parents,b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b

for edge in edges:
    cost,a,b=edge
    if find_parent(parents,a)!=find_parent(parents,b):
        union_parent(parents,a,b)
        ans+=cost

print(int(ans))