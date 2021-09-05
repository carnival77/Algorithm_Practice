import sys

coins = [500,100,50,10]

cnt=0
n=int(input())

for coin in coins:
    cnt += n // coin
    n = n % coin

print(cnt)