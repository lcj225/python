def t_converter():
    print("화씨 변환 프로그램")
    tem = float(input("섭씨온도 입력 : "))
    tem = round((tem * 1.8) + 32, 2)
    print(tem)
    return
