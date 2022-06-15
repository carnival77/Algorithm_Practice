import sys
input=sys.stdin.readline
n=int(input())

stack=[]

for _ in range(n):
    data = list(input().split())
    cmd = data[0]
    num=0
    if len(data)>=2:
        num=data[1]
    if cmd=="push":
        stack.append(num)
    elif cmd=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif cmd=="size":
        print(len(stack))
    elif cmd=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else:
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())