#숫자 야구 게임


import random

while True:
    goal_num1 = random.randrange(10)
    goal_num2 = random.randrange(10)
    goal_num3 = random.randrange(10)
    if goal_num1 != goal_num2 != goal_num3:
        break

goal_num = [goal_num1, goal_num2, goal_num3]


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
    
