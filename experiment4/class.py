# class Car(object):
#     def infor(self):
#         print("This is a car")
#
#
# car = Car()
# car.infor()
# print(isinstance(car, Car))
# print(isinstance(car, str))


# class A:
#     pass
# class demo():
#     pass
# if 5 > 3:
#     pass

class A:
    def __init__(self, value1=0, value2=0):
        self._value1 = value1
        self.__value2 = value2

    def setValue(self, value1, value2):
        self._value1 = value1
        self.__value2 = value2

    def show(self):
        print(self._value1)
        print(self.__value2)

a = A()
print(a._value1)
print(a._A__value2)
a.show()

class Car(object):
    price = 100000 #属于类的数据成员
    def __init__(self,c):
        self.color = c #属于对象的数据成员


car1 = Car("red") #实例化对象
car2 = Car('blue')
print(car1.color, Car.price) #访问对象和类的数据成员
Car.price = 290000 #修改类的属性
Car.name = "Su7" #动态增加类的属性
car1.color = 'yellow' #修改实例的属性
print(car2.color, Car.price, Car.name)
print(car1.color,car1.price, car1.name)


class Root:
    _total = 0
    def __init__(self, v):
        self._value = v
        Root._total += 1
    def show(self):
        print('self._value', self._value)
        print("self._total", self._total)

    @classmethod # 修饰器，声明类方法
    def classShowTotal(cls):
        print(cls._total)

    @staticmethod # 修饰器，声明静态方法
    def statisShowTotal():
        print(Root._total)

r = Root(3)
r.classShowTotal()
r.statisShowTotal()
r.show()

class Test:
    def __init__(self, value):
        self.__value = value
    @property
    def value(selfs):
        return selfs.__value
t = Test(3)
print(t.value)