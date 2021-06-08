str = input()

length = len(str)

sum = 0

for i in range(length//2):
    sum += int(str[i])

for i in range(length//2,length):
    sum -= int(str[i])

if sum ==0:
    print("LUCKY")
else:
    print("READY")