import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    stack=[]
    data=list(input().rstrip())
    ok=True
    for i in range(len(data)):
        if data[i]=='(':
            stack.append(data[i])
        elif data[i]==')':
            if len(stack)>0:
                stack.pop()
            else:
                ok=False
                break
    if len(stack)>0:
        ok=False
    if ok:
        print("YES")
    else:
        print("NO")