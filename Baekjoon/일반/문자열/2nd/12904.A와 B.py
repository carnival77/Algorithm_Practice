a=list(input())
b=list(input())
ans=0

while True:
    n = len(a)
    m = len(b)

    if n>m:
        ans=0
        break

    if a==b:
        ans=1
        break
    t=b.pop()
    if t=='B':
        b.reverse()

print(ans)