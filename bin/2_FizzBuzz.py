def t():
    for i in range(101):
        if (i % 3 == 0) & (i % 5 != 0):
            print("Fizz")
        elif (i % 3 != 0) & (i % 5 == 0):
            print("Buzz")
        elif (i % 3 == 0) & (i % 5 == 0):
            print("FizzBuzz")
        else:
            print(i)


def main():
    t()


if __name__ == '__main__':
    main()