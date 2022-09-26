def gugudan(num):
    if num < 10 and num > 0:
        for i in range(1, 10):
            print(num * i)


def back(str):
    ans = ""
    if str != "" or str is not None:
        ans = str[::-1]
    print(ans)


def binary(num):
    string = ""
    while (num != 1 and num != 0):
        string = string + str(num % 2)
        num = num // 2
        print(string, "   ", num)
    else:
        string = string + str(num)
    print(string)


# gugudan(int(input("숫자입력 : ")))
# back( input("입력 : "))
binary(int(input("숫자입력 : ")))
