import sys

input = sys.stdin.readline

n,m,seq= map(int,input().split())

a=[]
b=[]

for i in range(n):
    a.append(list(map(int,input().split())))
    b.append([])

cmd = int(input())

for i in range(n):
    print(a[i])

if cmd==1:
    for _ in range(seq):
        for i in range(n):
            next_i = (n-1) - i
            b[i] = a[next_i]

print()
for i in range(n):
    print(b[i])
