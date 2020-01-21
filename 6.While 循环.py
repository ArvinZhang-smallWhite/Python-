# 1
from random import randint

print("------猜大小数字游戏------")
input("点击Enter键后开始游戏")
start = True
num = randint(0, 100)
while start:
    guess = input("猜一个从0到100的数字，或者直接点击Enter键退出游戏！")
    if guess:
        guess = int(guess)
    else:
        break
    if guess > num:
        print("你猜的数太大了")
    elif guess < num:
        print("你猜的数太小了")
    else:
        print("Bingo! 你猜对了！")
        start = False
        
# 2
count = 0
while count<10:
    count += 1
    if 4 <= count <= 5:
        continue
    print(count)

# 3
n = 0
n_sum = 0
while n <= 100:
    n += 1
    if n % 3 == 0:
        n_sum += n
print(n_sum)
