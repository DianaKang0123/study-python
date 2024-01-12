'''
number = 15
# % = modulus
if number % 3 == 0:
    print(f'{number}는 3의 배수입니다.')
if number % 5 == 0:
    print(f'{number}는 5의 배수입니다.')

# number가 양수인지 음수인지 0인지 검사
number = 0
positive_condition = number > 0
negative_condition = number < 0

if positive_condition:
    print(f'{number}는 양수입니다.')
elif negative_condition:
    print(f'{number}는 음수입니다.')
else:
    print(f'{number}')

print("="*30)

# 나이를 입력 받은 후 미성년자인지 검사

message = '나이 : '

age = int(input(message))

teen_condition = 0 < age < 19
error_condition = age <= 0
if teen_condition:
    print('미성년자입니다.')
elif error_condition:
    print('잘 못 입력하였습니다.')
else:
    print('성인입니다.')
'''
'''
# 두 정수를 입력 받은 후 대소 비교 진행
message = '두 정수를 입력하세요\nex)1 2\n'
number1,number2=map(int,input(message).split())
condition1 = number1 > number2
condition2 = number1 < number2

if condition1:
    print(f'{number1}은 {number2}보다 큽니다.')
elif condition2:
    print(f'{number1}은 {number2}보다 작습니다.')
else:
    print('두 수는 같습니다.')

# if number1>number2:
#     print(f'큰 값{number1}')
# elif number1!=number2:
#     print(f'큰 값{number2}')
# else:
#     print('같습니다.')
'''


message = '두 정수를 입력하세요\nex)1 2\n'
number1,number2=map(int,input(message).split())
# 선언 시 넣을 값을 모를 경우 초기값을 넣어준다.
# 이 작업을 초기화라고 한다.
# 정수 -> 0
# 실수 -> 0.0
# 문자열 -> ''또는""
# 불린 -> false
result_message = ''

# 일괄처리란,
# 각 분기별로 결과를 처리하지 않고
# 모든 분기 종료후 한번에 처리하는 것을 의미한다.

if number1 > number2:
    result_message = f'{number1}은 {number2}보다 큽니다.'
elif number1 < number2:
    result_message = f'{number1}은 {number2}보다 작습니다.'
else:
    result_message = '두 수는 같습니다.'

print(result_message)


# if number1>number2:
#     print(f'큰 값{number1}')
# elif number1!=number2:
#     print(f'큰 값{number2}')
# else:
#     print('같습니다.')