a = input()

n=len(a)
cnt=1
result=''

for step in range(1,n//2+1):
    for i in range(0,n//2,step):
        if a[i:i+step] == a[i+step:i+2*step]:
            cnt+=1
        else:
            if cnt > 0:
                result+= str(cnt) + a[i:i+step]
            else:
                result+=a[i:i+step]
            cnt = 0

print(result)