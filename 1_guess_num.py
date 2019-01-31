import random


def x_input():
    while True:
        x = input("输入猜测：")
        try:
            t = int(x)
            if (t > 100) & (t < 1000):
                break
        except:
            print("输入不合格，请重新输入。")
            pass
    return t


def main():
    y = random.randint(100, 999)
    while True:
        x = x_input()
        if x>y:
            print("大了")
        elif x<y:
            print("小了")
        else:
            print("恭喜您猜对啦！")
            break



if __name__ == '__main__':
    main()
