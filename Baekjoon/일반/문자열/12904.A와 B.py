a=list(input())
b=list(input())
ans=0
while len(b)>0:
    if b[-1]=='A':
        b.pop(-1)
        if a==b:
            ans=1
            break
    else:
        b.pop(-1)
        b.reverse()
        if a==b:
            ans=1
            break
print(ans)