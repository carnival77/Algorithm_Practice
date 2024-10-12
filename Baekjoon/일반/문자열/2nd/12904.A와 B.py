# [풀이 시간]
# 2회 : 약 1시간

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