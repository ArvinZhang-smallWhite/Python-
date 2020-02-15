# 1
def func(x):
    print(x)
    return x + 1


x = 2
print(func(x))


# 2
def func(param):
    return param * 2


p = func(20)
print(p)

# 3
def combine(list1,list2):
    list_c=list1+list2
    list_c.sort()
    return list_c

print(combine([1,5,3], [2,6,7,4]))
