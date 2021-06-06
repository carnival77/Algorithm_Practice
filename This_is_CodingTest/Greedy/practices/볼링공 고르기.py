n,m = map(int,input().split())

data = list(map(int,input().split()))

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