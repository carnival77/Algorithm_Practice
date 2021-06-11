input_str = list(input())

# str.sort()

nums = ['1','2','3','4','5','6','7','8','9']

target_nums=[]

for i in input_str:
    for k in nums:
        if i == k:
            target_nums.append(i)
            input_str.remove(i)

sum = 0
for i in target_nums:
    sum+=int(i)

input_str.sort()

input_str.append(str(sum))

result = "".join(input_str)

print(result,end='')
