#가위바위보

import random


while True:
    com_choice = random.choice(['가위', '바위', '보'])
    user_choice=input("가위, 바위, 보 중 하나를 입력하세요.")

    if user_choice == '가위':
        if com_choice == '가위':
            print('프로그램: ', com_choice, "\n비겼습니다.\n")
        elif com_choice == '바위':
            print('프로그램: ', com_choice, "\n졌습니다.\n")
        elif com_choice == '보':
            print('프로그램: ', com_choice, "\n이겼습니다.\n")

    elif user_choice == '바위':
        if com_choice == '바위':
            print('프로그램: ', com_choice, "\n비겼습니다.\n")
        elif com_choice == '보':
            print('프로그램: ', com_choice, "\n졌습니다.\n")
        elif com_choice == '가위':
            print('프로그램: ', com_choice, "\n이겼습니다.\n")

    elif user_choice == '보':
        if com_choice == '보':
            print('프로그램: ', com_choice, "\n비겼습니다.\n")
        elif com_choice == '가위':
            print('프로그램: ', com_choice, "\n졌습니다.\n")
        elif com_choice == '바위':
            print('프로그램: ', com_choice, "\n이겼습니다.\n")

    else:
        print("입력이 바르지 않습니다.\n")
