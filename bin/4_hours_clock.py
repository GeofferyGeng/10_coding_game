import time


def main():
    t_vectot = [0, 1, 2, 3, 4, 5, 6]
    while True:
        t = time.localtime(time.time())
        print(t.tm_sec)
        if (t.tm_min == 0) & (t.tm_sec == 0):
            if t.tm_hour not in t_vectot:
                print("长")
        elif (t.tm_min == 30) & (t.tm_sec == 0):
            if t.tm_hour not in t_vectot:
                print("短")
        else:
            pass
        # 线程睡眠0.5s
        time.sleep(0.5)


if __name__ == '__main__':
    main()
