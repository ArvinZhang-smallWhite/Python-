# 1
sum_n = 0
for i in range(1, 101):
    if i % 3 == 0:
        sum_n += i
print("sum=", sum_n)

# 2
h = int(input("请输入矩形的高"))
k = int(input("请输入矩形的宽"))
if h > 0 and k > 0:
    for i in range(h):
        print("* " * k)
else:
    print("输入有误，请重新开始。")

# 3
for i in range(1, 10):
    for j in range(1, i + 1):
        print("# %d x %d = %d" % (i, j, i * j))

# 4
nums = [23, 45, 8, 13, 50, 43, 21]
nums_sum = 0
for i in nums:
    nums_sum += i
    print("i=", i)
    print("nums_sum=", nums_sum)
    if nums_sum > 100:
        break
