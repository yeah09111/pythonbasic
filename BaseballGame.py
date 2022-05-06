#숫자 야구 게임


import random

while True:
    goal_num1 = random.randrange(10)
    goal_num2 = random.randrange(10)
    goal_num3 = random.randrange(10)
    if (goal_num1 != goal_num2) and (goal_num2 != goal_num3) and (goal_num1 != goal_num3):
        break

#print(goal_num1, goal_num2, goal_num3)
goal_num = [goal_num1, goal_num2, goal_num3]


while True:
    count_ball = 0
    count_strike = 0

    for i in range(3):
        print("\n", i+1, "번째 숫자를 입력해 주세요.")
        inp_num = int(input())
        if inp_num in goal_num:
            if inp_num == goal_num[i]:
                count_strike+=1
            else:
                count_ball+=1
    print("\nball: ", count_ball)
    print("strike: ", count_strike)

    if count_strike == 3:
        print("\n홈런!")
        break
    
