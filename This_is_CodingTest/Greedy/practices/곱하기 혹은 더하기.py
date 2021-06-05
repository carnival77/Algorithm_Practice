str = input()

result = 0

for i in range(len(str)):
    num = int(str[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
