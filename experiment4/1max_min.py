import random


def create_list(length, start=0, end=10000):
    """
    :param length: lenth of the list
    :param start:
    :param end:
    :return: list
    """
    listRandom = [random.choice(range(start, end)) for i in range(length)]

    return listRandom


def get_max_min(list):
    """
    :param list:
    :return: max and min
    """
    max_values = max(list)
    min_values = min(list)
    return max_values, min_values


if __name__ == '__main__':
    rand_list = create_list(20)
    print(rand_list)
    max_values, min_values = get_max_min(rand_list)
    print('max:', max_values, 'min:', min_values)
    a_list = create_list(10, 0, 50)
    b_list = create_list(10, 0, 50)
    print(a_list,b_list)
    print("交集",set(a_list) & set(b_list))
    print("并集", set(a_list) | set(b_list))
