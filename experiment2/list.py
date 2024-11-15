import math

# a_list = ['a','b', 'python', 'gzj']
# print(a_list)


# # 转换
# a_list=list((3,5,6,7,2))
# print("from tuple to list",a_list)
# print('from range to list',list(range(1,10,2)))
# print(list('hello Python'))
# print('from set to list', list({3,4,5}))
# print('from dict to list', list({'a':3,'b':9,'c':78}))
# print('from dict items to list', list({'a':3,'b':9,'c':78}.items()))
# print('from dict value to list', list({'a':3,'b':9,'c':78}.values()))

##添加
# x = [1,2,3]
# print(x)
# x.append(4)
# print(x)
# x.insert(0, 0)
# print(x)
# x.extend([5,6,7])
# print(x)

##删除
# x=[1,2,3,4,1,2,7]
# print("pop:",x.pop(0))
# print(x)
# x.remove(1)
# print(x)
# x.clear()
# print(x)
# del x
# # print(x)

# x=[1,2,2,3,3,3,4,4,4,4]
# print(x.count(3))
# print(x.index(2))
#
# x=[6,0,1,7,4,3,2,8,5,10,9]
# x.sort()
# print(x)
# print(reversed(x))
# print(list(reversed(x)))

# #列表推导式 顺序从左到右
# aList=[x*x for x in range(10)]
# print(aList)
# #等价于
# aList = []
# for x in range(10):
#     aList.append(x*x)
# print(aList)
# #展开
# vec = [[1,2,3],[4,5,6],[7,8,9]]
# print(vec)
# print([num for elem in vec for num in elem])
#
# aList = [-6, -8, 4, -5, 1, 8, 3, 4, 22]
# print([i for i in aList if i>0])
# highest = max(aList)
# print(highest)
#
# scores = {'zhang san':45,'li si':78,'wang wu':40,'zhou liu':96,'zhao qi':65,'su ba':90,'zheng jiu':78,'wu shi':99,
# 'dong shiyi':60}
# highest=max(scores.values())
# print(highest)
# lowest = min(scores.values())
# print(lowest)
# average = sum(scores.values())/len(scores)
# print(average)
#
# highestPerson = [name for name,score in scores.items() if score == highest]
# print(highestPerson)


# #列表推导式
#
# print([(x,y) for x in [1,2,3] for y in [3,1,4] if x != y])
#
# result = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if  x != y:
#             result.append((x,y))
# print(result)
#
# #矩阵转置
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(matrix)
# print([[row[i] for row in matrix] for i in range(4)])
#
# #使用列表推导式生成 100 以内的所有素数
# print([p for p in range(2,100) if 0 not in [p%d for d in range (2,int(math.sqrt(p)) +1)]],end=" ")


# #切片
# aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
#
# #返回包含原列表中所有元素的新列表
# print(aList[::])
# #返回包含原列表中所有元素的逆序列表
# print(aList[::-1])
# #隔一个元素取一个元素，获取偶数位置的元素
# print(aList[::2])
# #指定切片的开始位置和结束位置
# print(aList[3:6])
# #切片的结束位置大于列表长度时，从列表尾部截断
# print(aList[0:100])
# #切片的开始位置大于列表长度时，返回空列表
# print(aList[100::])
#
# #在列表尾部增加元素
# aList[len(aList):] = [9]
# print(aList)
# #替换列表元素
# aList[:3] = [1, 2, 3]
# print(aList)
# #删除列表元素
# aList[:3] = []
# print(aList)
# #使用 list 生成列表
# aList = list(range(10))
# print(aList)
# #替换列表元素   // 为向下取整除
# aList[::2] = [0] * (len(aList) // 2)
# print(aList)
# #在列表指定位置插入元素
# aList[3:3] = [4, 5, 6]
# print(aList)
# #在列表尾部追加元素
# aList[20:30] = [3] * 2
# print(aList)
# #结合使用 del 命令与切片结合来删除列表中的部分元素
# aList = [3, 45, 7, 9, 11]
# del aList[:3]
# print(aList)
#
#
# #bList 与 aList 指向同一内存
# aList = [3, 5, 7]
# bList = aList
# print(bList)
# bList[1] = 8
# print(aList)
#
# #两个列表的值是相等的
# print(aList==bList)
#
# print(aList is bList)
#
# #两个列表的内存地址相等
# print('id', id(aList)==id(bList))
#
# #切片浅复制,不是同一个对象
# aList=[3,5,7]
# bList=aList[::]
# print(aList == bList)
# print(aList is bList)
# print('id', id(aList)==id(bList))
# print(id(aList[0])==id(bList[0]))
#
# #修改 bList 列表元素的值不会影响 aList
# bList[1]=8
# print(bList)
# print(aList)
# print(aList==bList)
# print(aList is bList)
#
#
# #虽然直接把一个列表变量赋值给另一个变量时两个变量指向同一个内存地址， 但是把一个列表分别赋值给 2 个变量时就不是这样的情况了，如：
# x = [1,2,3]
# y = [1,2,3]
# print(id(x)==id(y))
# y.append(4)
# print(y)
# print(x)
#
#
# #然而，当列表中包含其它可变序列时，情况变的更加复杂，如：
# x=[[1],[2],[3]]
# y=x[:]
# print(y)
# y[0]=[4]
# print(y)
# y[1].append(5)
# print(y)
# print(x)

#元组
x=(1,2,3)
print(x)
print(type(x))
x=(3,)
print(x)
#将其他迭代对象转换为元组
print(tuple(range(5)))
#一般元组中元素的值是不可变的，但当元组中包括可变的列表的时候，是可修改元组中列表元素的。
x=([1,2],3)
x[0][0]=5
print(x)
x[0].append(8)
print(x)



