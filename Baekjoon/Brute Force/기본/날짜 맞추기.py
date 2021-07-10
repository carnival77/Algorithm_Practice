import sys
a,b,c = map(int,input().split())

e,s,m = 1,1,1

stop=False

answer = 1

while (stop != True):
    if e == 16:
        e=1
    if s == 29:
        s=1
    if m==20:
        m=1
    if a == e and b == s and c == m:
        print(answer)
        sys.exit(0)
    e+=1
    s+=1
    m+=1
    answer += 1