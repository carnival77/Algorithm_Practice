a1 = [3,1,1]
a1=[2,1,3]

def cnt_num(a):
    b1 = []
    for i in range(1, 101):
        if a1.count(i) > 0:
            b1.append((i, a1.count(i)))
    return b1


def sort_func(a):
    return sorted(a,key = lambda x : (x[1],x[0]))


def make_list(a):
    temp = []
    for i in a:
        x, y = i
        temp.append(x)
        temp.append(y)
    return temp

def sort_arr(a):
    return make_list(sort_func(cnt_num(a)))

result = sort_arr(a1)

print("result :",result)
#
# a=[(3,1),(1,2),(2,1),(4,2)]
#
# b = sorted(a,key = lambda x : (x[1],x[0]))
#
# print("".join(str(b)))