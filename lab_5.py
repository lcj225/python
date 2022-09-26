def gugu(num):
    if num > 0 and num < 10:
        for i in range(1, 10):
            print(num * i)


def game():
    x = 10
    while x != 0:
        try:
            x = int(input("숫자입력(1~9) : "))
            while x >= 10 or 0 > x:
                x = int(input("다시입력(1~9) : "))
        except ValueError:
            print("정수로 입력하시오")
        gugu(x)
    else:
        print("종료")


def avr():
    lst = ["국", "영", "수", "과"]
    ans = []
    x = "y"
    num = 0
    while x == "y":
        score = []
        for j in range(0, len(lst)):
            score.append(int(input(lst[j] + " 점수입력 : ")))
        ans.append(score)
        x = input("더 입력 할 경우 y를 입력 : ")
    else:
        for i in range(0, len(ans)):
            for k in range(0, 4):
                num = num + ans[i][k]
            print(str(i + 1) + "번 사람 : " + str(round(num / 4, 3)))
            num = 0


game()
avr()
