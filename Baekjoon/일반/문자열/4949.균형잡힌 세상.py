import sys
input=sys.stdin.readline

open=['(','[']
close=[')',']']
while True:
    a = input().rstrip()
    stack = []
    if len(a)==1 and a[0]=='.':
        break
    ok = True
    for i in a:
        if i in open:
            stack.append(i)
        elif i in close:
            if len(stack)>=1:
                if i==')' and stack[-1]=='(':
                    stack.pop()
                elif i==']' and stack[-1]=='[':
                    stack.pop()
                else:
                    ok=False
            else:
                ok=False
    if len(stack)>=1:
        ok=False
    if ok:
        print('yes')
    else:
        print('no')