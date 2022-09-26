def counter(string):
    check = input("확인할 문자열 : ")
    a = 0
    for i in string:
        a = a + i.count(check)
    return a


print("입력시작 :")
string = [input()]
while string[len(string)-1] != "끝":
    string.append(input())
else:
    string.remove("끝")
    print(counter(string))