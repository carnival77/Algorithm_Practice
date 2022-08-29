from collections import Counter
import sys

data=[]
while True:
    tree=sys.stdin.readline().rstrip()
    if tree == '':
        break
    else:
        data.append(tree)
a=list(Counter(data).items())
a.sort()

for x,y in a:
    print("%s %.4f"%(x,y/len(data)*100))