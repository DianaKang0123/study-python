# 사용자가 입력한 정수가 몇자리 수인지 출력
# 정수 입력
# 각자리 수 세기
# 자리 수 출력
# 몫과 나머지
# message = '정수를 입력하세요\n'
# number = int(input(message))
# length = 0
# while number > 0:
#     number //= 10
#     length += 1
# print(length)

# 문자열의 길이를 for 문으로

# if문 문제
# 숫자를 입력받아 짝수인지 홀수 인지 출력

message1='숫자를 입력하세요\n'
number = int(input(message1))
if number % 2==0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

# for문 문제
# 크리스마스 트리만들기
line = int(input("Tree 의 높이를 입력하세요(5~30) : "))

for x in range(1, line * 2, 2):
    print((" " * ( (line * 2 - 1 - x) // 2 )) + ("*" * x))

# while문 문제





