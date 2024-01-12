# # f(x) = 2x+1
#
# # def f(x):
# #     return 2 * x + 1
# #
# # result = f(2)
# # print(result)
#
# # 두 정수의 곱셈
#
# def times(number1, number2):
#     result = number1 * number2
#     return result
#
# # 두 정 수의 나눗셈 후 몫과 나머지를 구하는 함수
#
# def devide(number1, number2):
#     if number2 != 0:
#         value = number1//number2
#         share = number1 % number2
#         return value, share
#     return None
#
# # 1~10까지 print()로 출력하는 함수
#
# def print_number_to10():
#     for number in range(10):
#         number += 1
#         print(number, end=",")
#
# # 1~n까지의 합을 구해주는 함수
#
# def get_totalsum(end):
#     result = 0
#     for number in range(end):
#         result += number+1
#     return result
#
# # 이름을 n번 print()로 출력하는 함수
# def print_names(name, repeat):
#     for i in range(repeat):
#         print(name)
#
# # 1~100까지중 n의 배수를 print()로 출력하는 함수
#
# def fine_multiply(n):
#     for number in range(100):
#         number += 1
#         if number % n == 0:
#             print(number)
#
# # 세 정수의 뺄셈 함수
#
# def minus(number1, number2, number3):
#     return number1-number2-number3
# #list를 활용 할 수 도 있음(numbers)
#
#
# # 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수
# def count_letter(string, letter):
#     # return len([i for i in string if i == letter])
#     count = 0
#     for l in string:
#         if l == letter:
#             count +=1
#     return count
#
# '''
# 문자열과 문자를 입력받은 뒤 해당 문자가 몇번 째 인덱스에 있는지 검사하고,
# 만약 해당 문자가 없으면 -1을 리턴하는 함수
# '''
#
# def find_letter_index(string, letter):
#     return string.find(letter)
#
# def find_letter1(targer, keyword):
#     for i in range(len(targer)):
#         if targer[i] == keyword:
#             return i
#     return -1
#
# def find_letter2(targer, keyword):
#     result = -1
#     for i in range(len(targer)):
#         if targer[i] == keyword:
#             result = i
#             break
#     return result
#
