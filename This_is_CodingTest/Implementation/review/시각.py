n = int(input())

ans=0

for h in range(n+1):
    # H = list(str(h))
    # if '3' in H:
    #     ans+=1
    for m in range(60):
        # M = list(str(m))
        # if '3' in M:
        #     ans+=1
        for s in range(60):
            H = list(str(h))
            M = list(str(m))
            S = list(str(s))
            if '3' in S or '3' in H or '3' in M:
                ans+=1

print(ans)