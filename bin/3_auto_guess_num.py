import random
import math


# 二分法逼近
def method_1():
    b = 100
    c = 1000
    a = round((b + c) / 2)
    y = random.randint(b, c)
    i = 0
    while True:
        i = i + 1
        if a > y:
            c = a
            a = math.floor((c + b) / 2)
        elif a < y:
            b = a
            a = math.ceil((c + b) / 2)
        else:
            print("恭喜您猜对啦！")
            break
    print("经过 ", i, " 次猜对，猜中数字为：", y)


# 暂时没有找到更好的算法
def method_2():
    b = 100
    c = 1000
    y = random.randint(b, c)
    i = 0


def main():
    method_2()


if __name__ == '__main__':
    main()
