n,m = map(int,input().split())

data = list(map(int,input().split()))

# solution 1

result = n*(n-1) / 2

print(result)

overlap = set([])

for i in data:
    if data.count(i) >= 2:
        overlap.add(i)

print(overlap)

for i in overlap:
    n = data.count(i)
    result -= n*(n-1) / 2

print(int(result))

# solution 2

n,m = map(int,input().split())

data = list(map(int,input().split()))

result=0

arr = [0]*11
for i in data:
    arr[i] += 1

for i in range(1,m+1):
    n -= arr[i]
    result += n * arr[i]

print(result)