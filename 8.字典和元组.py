# 1
data = {
    'one': 1,
    'two': 2,
    'three': 3,
}

data['two'] = 4

print(data)
# 2
words = 'Beautiful is better than ugly Explicit is better than implicit Simple is better than complex Complex is better than complicated Flat is better than nested Sparse is better than dense'
word = words.split()
dic = {}
for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in dic:
    print('%s:%d'%(i,dic[i]))

#Beautiful:1
#is:6
#better:6
#than:6
#ugly:1
#Explicit:1
#implicit:1
#Simple:1
#complex:1
#Complex:1
#complicated:1
#Flat:1
#nested:1
#Sparse:1
#dense:1
