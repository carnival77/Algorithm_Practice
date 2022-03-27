import sys

input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break
    num=0
    cnt=1
    while True:
        num = num*10 + 1
        num = num % n
        if num == 0:
            print(cnt)
            break
        cnt+=1