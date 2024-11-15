def fib(n):
    a, b = 1, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def linear(a, b):
    a, b = 1, 1

    def result(x):
        return a * x + b

    return result(2)


def addOne(a):
    print(a)
    a += 1
    print(a)


def modify(v):
    v[0] += 1
    # v[0] = v[0] + 1


def modify2(v, item):
    v.append(item)


def modify3(v):
    v['age'] = 38


def demo(n):
     return n * n


class Linear:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __call__(self, x):
        return self.a * x + self.b


if __name__ == '__main__':
    # a = 3
    #
    # addOne(a)
    # print(a)
    #
    # b = [3]
    # modify(b)
    # print(b)
    # modify2(b, 1)
    # print(b)
    #
    # c = {'name': 'Dong', 'age': 37, 'sex': 'Male'}
    # modify3(c)
    # print(c)
    #
    # print("linear by funciton:", linear(1, 1))
    # test = Linear(1, 1)
    # print("linear by class:", test(2))
    # fib(10)
    #
    # a_list = [1, 2, 3, 4, 9, 5, 7]
    # print(sorted(a_list))
    # print(a_list)
    # print(a_list.sort())
    # print(a_list)

    f = lambda x, y,z : x + y + z
    print(f(1,2,3))
    g = lambda x, y = 2, z = 3: x + y + z
    print(g(1))
    print(g(2, z = 4, y = 5))
    L = [1, 2, 3, 4, 5]
    print(map(lambda x : x + 10, L))

    a_list = [1, 2, 3, 4, 5]
    print(list(map(lambda x : demo(x), a_list)))


