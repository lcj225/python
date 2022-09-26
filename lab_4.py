import random


def game():
    ans = random.randrange(1, 100)
    x = 0
    print("1~100까지 입력")
    while x != ans:
        x = int(input("숫자입력 : "))
        if x > ans:
            print("크다")
        else:
            print("작다")
    else:
        print("정답 :", ans)

game()