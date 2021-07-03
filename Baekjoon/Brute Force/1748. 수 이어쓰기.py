import sys

n=input()

length = len(n)

result=0

while length>0:
   result+= length * (int(n)-pow(10,(length-1)) +1)
   n = pow(10,(length-1)) -1
   length-=1

print(result)