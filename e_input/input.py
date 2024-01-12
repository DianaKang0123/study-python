# 문자열의 연결
# 문자열 끼리만 연결이 가능. 연산자 + 사용
data = 3
print("안"+str(data))

name = input("이름: ")
formatting = f'{name}님 환영합니다.'
print(formatting)

# 제 이름은 ???, 키는 ???cm 입니다.
name = input("이름 : ")
height = input("키 : ")
formatting = f'제 이름은 {name}, 키는 {height}cm 입니다.'
print(formatting)

# 두 정수를 입력받은 후 곱셈 결과 출력
print("두 정수의 곱셈")
msg1 = '첫번째 정수 : '
msg2 = '두번째 정수 : '

num1 = int(input(msg1))
num2 = int(input(msg2))

result = (num1 *num2)

formatting = f'두 정수의 곱은 {result}이다.'

print(formatting)

# map => 반복문
# map에 전달되는 값은 무조건 함수가 첫번째로 들어가야함 = 이름 뒤에 소괄호가 있으면 함수이다.
# map(어떻게 바꿀것인가, [])
# split - 값을 나누어 구분해주는 문자열 함수
# 값은 list의 형식으로 나타남

# advanced(**)
num1, num2 = map(int,input ('두 정수를 입력하세요\n ex)1, 3\n').split(','))
print(num1 * num2)

message='두 정수를 입력하세요.'
example_message = "ex) 1, 3"
number1, number2 = map(int, input(message+'\n'+example_message+'\n').split(', '))
result = number1*number2
formatting = f'{number1}*{number2} = {result}'
print(formatting)

# 현재 시간을 입력하고 시와 분으로 분리하여 출력

message = '현재 시간\nex) 10:35\n'
time = input(message)
hour,minute = map(int,time.split(":"))
formatting = f'현재는 {hour}시 {minute}분 입니다.'
print(formatting)

print("="*30)

# 핸드폰 번호를(-)하이픈과 함께 입력 받은 뒤 각 자리의 번호를 분리해서 출력

massage='핸드폰 번호를 입력하세요.\n ex)010-1234-5678\n'

num1,num2,num3=input(massage).split('-')

formatting = f'통신사: {num1}\n앞번호 : {num2}\n뒷번호 : {num3}'

print(formatting)

print("="*20)

# 이름 과 나이를 입력 받은 후 000님의 나이는 000살 형식으로 출력

massage1 = '이름과 나이를 입력 하세요.'
example_message1 = 'ex) 홍길동 23세'

name, age = input(massage1+'\n'+example_message1+'\n').split()
formatting = f' 귀하의 이름은 {name}, 나이는 {age}세 입니다.'

print(formatting)

print("="*20)

# 3개의 정수를 입력 받은 뒤 덧셈 결과 출력

massage2 = '세 정수를 입력하세요\nex) 1, 2, 3\n'

num1, num2, num3 = map(int, input(massage2).split(', '))
sum = num1+num2+num3

formatting = f'{num1}+{num2}+{num3}={sum}'

print(formatting)
