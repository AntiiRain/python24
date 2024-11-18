class Person(object):
    def __init__(self, na, gen, age, atk):
        self.name = na
        self.gender = gen
        self.age = age
        self.atk = atk

    def grassland(self):
        self.atk -= 200

    def practice(self):
        self.atk += 200

    def incest(self):
        self.atk -= 500

    def detail(self):
        temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力: %s" % (self.name, self.gender, self.age, self.atk)
        print(temp)

if __name__ == '__main__':
    fang = Person('小芳', '女', 18, 1000)
    gang = Person('小刚', '男', 20, 1800)
    jing = Person('小静', '女', 19, 2500)
    fang.incest()
    gang.practice()
    jing.grassland()

    fang.detail()
    gang.detail()
    jing.detail()
    print('-' * 30)
    fang.incest()
    gang.incest()
    jing.practice()

    fang.detail()
    gang.detail()
    jing.detail()
