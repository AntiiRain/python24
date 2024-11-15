# #创建
# a_dict={"server":"db.diveintopython3.org",'database':'mysql'}
# print(a_dict)

# keys=['a','b','c','b']
# values=[1,2,3,4]
# dictionary=dict(zip(keys,values))
# test = zip(keys,values)
# test
# print(dictionary)
#
# x=dict()
# print(x)
# print(type(x))
#
# d=dict(name='Dong',age=37)
# print(d)
#
# adict=dict.fromkeys(["name","age","sex"])
# print(adict)
#
# #当指定键为下标为字典元素赋值时，有两种含义：①若该“键”存在，则表示修改该“键”对应的值，
# # ②若该“键”不存在，则表示添加一个新的“键：值”，也就是添加一个新元素。
# #修改
# aDict=dict(name="Dong",age=38,sex="male")
# aDict['age']=38
# print(aDict)
# #添加
# aDict['address']="SDIBT"
# print(aDict)
#
aDict={"name":"Dong","score":[98,97],"age":38,"sex":"male"}
print(aDict.items())
aDict.update({"a": 97, "age": 39})
print(aDict)



del aDict['age']
print(aDict)
#删除整个列表
del aDict
# print('aDict',aDict)


aDict={"name":"Dong","score":[98,97],"age":38,"sex":"male"}
print(aDict.pop('sex'))
#优先弹出最末尾的
print(aDict.popitem())
print(aDict)

aDict={"name":"Dong","score":[98,97],"age":38,"sex":"male"}
print(aDict['age'])

# print(aDict['address'])
#配合条件判断或者异常处理结构 防止报错产生
if 'age' in aDict:
    print(aDict['age'])
else:
    print('Not exists')
try:
    print(aDict['address'])
except Exception as e:
    print('not exists by try catch')

#get()方法返回字典中指定“键”的值，并且允许指定该键不存在时返回特定的值
print('get age:',aDict.get('age'))
aDict.get('address', 'not exists')
print(aDict)
#setdefault()方法用于返回指定“键”对应的的“值”，如果字典中不存
#在该“键”，就添加一个新元素，并设置该键对应的值
print(aDict.setdefault('address','SDIBT'))
print(aDict)

aDict=dict(age=37,name="Dong",score=[98,97],sex='male')
for key in aDict:
    print(key)
for item in aDict.items():
    print(item)


print(aDict.keys())
print(aDict.values())

#字典的综合案例
import string
import random

x=string.ascii_letters+string.digits+string.punctuation
print(x)
y = [random.choice(x) for i in range(1000)]
z = ''.join(y)
d = dict()
for ch in z:
    d[ch] = d.get(ch, 0) + 1
print(d)

#拓展知识一：内置函数 globals()和 locals()分别返回包含当前作用域内所有全局变
#量和局部变量的名称及值的字典

a = (1,2,3,4)
b = 'hello world'
def demo():
    a = 3
    b = [1, 2, 3]
    print(a)
    print('locals:', locals())
    print('globals', globals())

demo()

#demo 2
phone_book = {'Linda':'7750','Bob':'9345','Carol':'5834'}
from operator import  itemgetter
#itemgetter 迭代器
#按字典的“值”进行排序
print(sorted(phone_book.items(),key = itemgetter(1)))
#按字典的“键”进行排序
print(sorted(phone_book.items(), key = itemgetter(0)))
#按字典的“键”进行排序
print(sorted(phone_book.items(),key =lambda item:item[0]))

persons=[{'name':'Dong','age':37},{'name':'Zhang','age':40},{'name':'Li','age':50},{'name':'Dong','age':18}]
print(persons)
#使用 key 来指定排序依据，先按姓名升序排序，姓名相同的年龄降序排序
print(sorted(persons, key=lambda x:(x['name'],-x['age'])))
#拓展知识三： Python 支持字典推导式快速生成符合特定条件的字典。
print({i:str(i) for i in range(1,5)})
x=['A','B','C','D']
y=['a','b','c','d']
print({i:j for i,j in zip(x,y)})