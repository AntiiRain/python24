
def get_gdc(x,y):
    gdc = 1
    tmp = 2
    half = min(x,y)/2
    while tmp <= half:
        if x%tmp == 0 and y%tmp == 0:
            gdc *=tmp
            x = x / tmp
            y = y / tmp
        else:
            tmp+=1
    return gdc

    # #使用小学学过的辗转相除法
    # while y != 0:
    #     x, y = y, x %y
    # return  x



def get_lcm(x,y,dgc):
    return int(x*y/dgc)
if __name__ == '__main__':
    x, y = 4, 8
    print(x,y)
    gdc = get_gdc(x,y)
    print("gdc = ", gdc)
    lcm = get_lcm(x,y,gdc)
    print('lcm = ',lcm)

    a, b = 3, 7
    print(a,b)
    gdc = get_gdc(a,b)
    print("gdc = ", gdc)
    lcm = get_lcm(a,b,gdc)
    print('lcm = ',lcm)








