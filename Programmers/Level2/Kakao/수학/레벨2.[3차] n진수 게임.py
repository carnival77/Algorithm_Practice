import string
tmp=string.digits+string.ascii_uppercase
def convert(num,base):
    q,r=divmod(num,base)
    if q==0:
        return tmp[r]
    else:
        return convert(q,base)+tmp[r]

def solution(n, t, m, p):
    ans = ''
    all=''
    cnt=1
    num = 0
    while len(ans)<t:
        inx=(p-1)+m*(cnt-1)
        if inx>=len(all):
            all+=convert(num,n)
            num += 1
        else:
            ans+=all[inx]
            cnt+=1

    return ans

# n=2
n=16
# t=4
t=16
m=2
# p=1
p=2
print(solution(n,t,m,p))