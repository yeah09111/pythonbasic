#function

def repeat():

    a=int(input("10 이하의 첫번째 정수를 입력해 주세요."))
    b=int(input("10 이하의 두번째 정수를 입력해 주세요."))

    for i in range(1,a+1):
        for j in range(1,b+1):
            print(i,j)


def test():
    
    score=int(input("점수를 입력해 주세요."))

    if score>=90:
        print("A")
    elif score>=70:
        print("B")
    elif score>=40:
        print("C")
    else:
        print("B")


def rocksp():
    
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


def baseball_game():
    
    import random

    while True:
        goal_num1 = random.randrange(10)
        goal_num2 = random.randrange(10)
        goal_num3 = random.randrange(10)
        if goal_num1 != goal_num2 != goal_num3:
            break

    goal_num = [goal_num1, goal_num2, goal_num3]

    #print(goal_num)

    while True:
        count_ball = 0
        count_strike = 0

        inp_num=input("세 자리 숫자를 입력해 주세요(숫자 중복X). ")

        for i in range(3):
            if int(inp_num[i]) in goal_num:
                if int(inp_num[i]) == goal_num[i]:
                    count_strike+=1
                else:
                    count_ball+=1
        print("\nball: ", count_ball)
        print("strike: ", count_strike)

        if count_strike == 3:
            print("\n홈런!")
            break


def main():
    a=input("숫자를 입력하세요 (1=이중반복문, 2=성적, 3=가위바위보, 4=숫자야구)")
    if a=='1':
        repeat()
    elif a=='2':
        test()
    elif a=='3':
        rocksp()
    elif a=='4':
        baseball_game()
    else:
        print("입력 오류")
        main()



main()
