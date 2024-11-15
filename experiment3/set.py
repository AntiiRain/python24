

a_set = {3, 4}
print(a_set)
print(type(a_set))

a_set = set(range(8,14))
print(a_set)
#自动去重复
b_set=set([0,1,2,3,4,0,1,2,3,7,8])
print(b_set)
x = set()
print(x)

#增加与删除
s = {1,2,3}
b_set=set([0,1,2,3,4,0,1,2,3,7,8])
#添加单个元素，重复元素自动忽略
s.add(3)
print(s)
#update 通过数据类型更新 重复自动忽略
s.update({3,4})
print(s)
s.update((5,6))
print(s)
##删除元素，元素不存在则忽略该操作
s.discard(7)
#删除指定元素，元素不存在就抛出异常
try :
    s.remove(7)
except Exception as e:
    print("do not exsist ")
print('pop',s.pop())
print(s)
s = {2,3}
print('pop',s.pop())

s = {1, 2, 3, 4}
print(s)
print('pop',s.pop())
#测试pop 随机性
for i in range(10):
    s = {1, 2, 3, 4}
    print('pop', s.pop())
    fruits = {"apple", "banana", "cherry"}
    print(fruits.pop())

fruits = {"apple", "banana", "cherry"}
print(fruits.pop())

a_set=set([8,9,10,11,12,13])
b_set=set([0,1,2,3,4,7,8])
#并集
print(a_set | b_set)
print(a_set.union(b_set))
#交集
print(a_set.intersection(b_set))
print(a_set & b_set)
#差集
print(a_set.difference(b_set))
print(a_set - b_set)
#对称差集
print(a_set.symmetric_difference(b_set))
print(a_set ^ b_set)


#关系运算符>,>=,<,<=作用于集合时表示集合之间的包含关系，而不是集合中元素比较大小。
x={1,2,3}
y={1,2,5}
z={1,2,3,4}
print(x < y)
print(x < z)
print(y < z)

print(x.issubset(y))
print(x.issubset(z))

import random
listRandom=[random.choice(range(200)) for i in range(100)]

no_repeat = []
for i in listRandom:
    if i not in no_repeat:
        no_repeat.append(i)
print(len(listRandom))
print(len(no_repeat))

new_set = set(listRandom)
print(new_set)