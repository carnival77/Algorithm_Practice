from itertools import combinations

l,c = map(int,input().split())

arr=list(map(str,input().split()))
arr.sort()

vowels=['a','e','i','o','u']

def check(a):
    cons_cnt=0
    ok1=False
    for i in a:
        if i in vowels:
            ok1=True
        else:
            cons_cnt+=1
    if cons_cnt>=2 and ok1:
        return True

    return False

for p in combinations(arr,l):
    p=list(p)
    if check(p):
        print("".join(p))