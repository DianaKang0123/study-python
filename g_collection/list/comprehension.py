# Comprehension(컴프리헨션 :어떤뜻을 내포[포함])
# 반복하거나 특정조건을 만족하는 list를 보다 쉽게 만들어 내기 위한 방법

# List Comprehension
# [표현식 for 항목 in iterator (if 조건)]
# iterator = 값이 여러 개이거나, 순서가 있는 집합
# number_list = [1,2,3,4]
# 각 요소에 3씩 곱하고 싶을 때
# for number in number_list:
#     number = number * 3
#     print(number)
# 위 식을 아래 처럼 표현가능
# result_list = [num *3 for num in number_list]
# print(result_list)

# number_list = [1,2,3,4]
#[6,12]
# result_list = [number * 3 for number in number_list if number % 2 == 0]
# print(result_list)

#[표현식 if 조건 else 표현식 for 항목 in iterator]
#[1,6,3,12]
number_list = [1,2,3,4]
result_list = [number * 3 if number % 2 == 0 else number  for number in number_list]
print(result_list)

# 아래 list에서 양수만 추출한 뒤 새로운 list 에 담기
# number_list = [10,20,30,-20,-3,50,-70]
# positive_list = [number for number in number_list if number > 0]
# print(positive_list)

# n 개의 0으로만 채워진 list
# 사용자의 숫자입력
# message = int(input('리스트 칸수 입력: \n'))
# # 입력한 숫자만큼의 리스트 생성
# number_list = list(range(message))
# # 리스트에 0인 값을 넣음
# result = [0 for number in number_list]
# print(result)
# message = '리스트 칸수 입력: \n'
# length = int(input(message))
# # result_list = [0 for i in range(length)]
# # print(result_list)
# result_list = [0] * length
# print(result_list)


# 제곱의 결과가 10보다 큰 결과만 담은 list
# list 선언
number_list = [1,-2,3,-4,5]
# 제곱을 했을 때 10이 넘는 수를 제곱한 값으로 리스트에 넣기
duple_list = [number for number in number_list if (number**2) > 10]
print(duple_list)

# 0~9까지 중 3의 배수만 담은 list
# 0 이상일 때 3의 배수가 담긴 리스트 생성
result_list = [number for number in range(10) if number % 3 == 0 and number > 0]
print(result_list)
