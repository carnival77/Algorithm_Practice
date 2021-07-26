from itertools import combinations,permutations

while(1):
    data = list(map(int,input().split()))

    if data[0] == 0:
        break

    k = data[0]
    arr = data[1:]

    results=set()

    combis = combinations(arr,6)
    for combi in combis:
        temp = list(combi)
        temp.sort()
        result = " ".join(list(map(str,temp)))
        print(result)
    print()

