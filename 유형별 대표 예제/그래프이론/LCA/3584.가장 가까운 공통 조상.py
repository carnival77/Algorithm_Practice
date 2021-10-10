import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):

    n=int(input())

    parent = [0] * ( n+1)

    for _ in range(n-1):
        p,c = map(int,input().split())
        parent[c] = p

    a,b = map(int,input().split())
    a_parents = [a]
    b_parents = [b]

    while parent[a]:
        a_parents.append(parent[a])
        a=parent[a]

    while parent[b]:
        b_parents.append(parent[b])
        b=parent[b]

    a_level = len(a_parents)-1
    b_level = len(b_parents) -1

    while a_parents[a_level] == b_parents[b_level]:
        a_level-=1
        b_level-=1

    print(a_parents[a_level+1])


# 참고 소스
#출처 : https://developmentdiary.tistory.com/467
import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):

    n=int(input())

    parent = [0] * ( n+1)

    for _ in range(n-1):
        p,c = map(int,input().split())
        parent[c] = p

    a,b = map(int,input().split())
    a_parents = [a]
    b_parents = [b]

    while parent[a]:
        a_parents.append(parent[a])
        a=parent[a]

    while parent[b]:
        b_parents.append(parent[b])
        b=parent[b]

    a_level = len(a_parents)-1
    b_level = len(b_parents) -1

    while a_parents[a_level] == b_parents[b_level]:
        a_level-=1
        b_level-=1

    print(a_parents[a_level+1])

