#10 이하의 두 개 의 정수가 입력됐을 때 나올 수 있는 모든 경우를 출력

a=int(input("10 이하의 첫번째 정수를 입력해 주세요."))
b=int(input("10 이하의 두번째 정수를 입력해 주세요."))

for i in range(1,a+1):
    for j in range(1,b+1):
        print(i,j)
