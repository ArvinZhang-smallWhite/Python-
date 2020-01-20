#1
money=88
if(money>100):
    print("rich")
else:
    print("pool")

#2
    #a  会输出True
    #b  输出False
    #c  如果有输入内容则输出为True，如果只敲回车，则输出False
    #d
    a = True
    b = not a  # 不记得not请回顾第二课
    print(b)  #False
    print(not b)  #True
    print(a == b)  #False
    print(a != b)  #True
    print(a and b) #False
    print(a or b)  #True
    print(1 < 2 and b == True) #False

#3
print("BMI计算器")
weight=int(input("请输入您的体重/公斤"))
height=float(input("请输入您的身高/米"))
bmi=float(weight/pow(height,2))
print("您的BMI指数为：%.1f"%bmi)
if(bmi<18.5):
    print("您的体重偏轻")
elif(bmi>=24):
    print("您的体重偏重")
else:
    print("您的体重正常")
