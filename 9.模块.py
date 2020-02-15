# 1
import math

r = 20
s = math.pi * math.pow(r, 2)
s = round(s, 2)
print(s)

# 2
import random

m = 0
l = []
for i in range(10):
    num = random.randrange(100)
    l.append(num)
    m = max(num, m)
print(l)
print(m)

# 3

num = random.randrange(100)
times=0
while True:
    guess = int(input('请输入你要猜的数：'))
    if num>guess :
        print('你猜的数太小了.')
        times+=1
    elif num<guess :
        print('你猜的数太大了.')
        times+=1
    else :
        print('Bingo!你猜对了！')
        times+=1
        break
print('恭喜！仅用%d次就猜对了。'%times)
