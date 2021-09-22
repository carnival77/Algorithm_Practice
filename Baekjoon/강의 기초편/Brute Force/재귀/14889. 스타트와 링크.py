n=int(input())

s=[]

for i in range(n):
    s.append(list(map(int,input().split())))

first=[]
second=[]

def recur(index, first, second):
    if index == n:
        if len(first) != n // 2: return -1
        if len(second) != n // 2: return -1

        t1 = 0
        t2 = 0

        for i in range(n // 2):
            for j in range(n // 2):
                if i == j: continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1-t2)
        return diff

    ans = -1
    t1 = recur(index+1, first+[index],second)
    if ans==-1 or (t1 != -1 and ans>t1):
        ans = t1
    t2 = recur(index+1, first, second+[index])
    if ans==-1 or (t2 != -1 and ans>t2):
        ans = t2
    return ans

print(recur(0,first,second))