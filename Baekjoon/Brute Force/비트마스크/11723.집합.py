import sys
input = sys.stdin.readline

m=int(input())
s=0
for _ in range(m):
    op,*temp = input().split()
    if(len(temp)>0):
        x=int(temp[0])-1
    if op=='add':
        s = (s | (1 << x))
    elif op=='remove':
        s = (s & ~(1 << x))
    elif op =='toggle':
        s = (s ^ (1 << x))
    elif op == 'check':
        res = (s & (1 << x))
        if res==0:
            sys.stdout.write('0\n')
        else:
            sys.stdout.write('1\n')
    elif op == 'all':
        s = ((s >> 20) -1)
    else:
        s =0
