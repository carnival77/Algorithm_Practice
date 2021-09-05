n,m = map(int,input().split())

result = 0

for _ in range(n):
    cur_max = min(list(map(int,input().split())))
    result = max(cur_max,result)

print(result)