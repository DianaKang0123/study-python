animals = ["dog", "cat", "bird", "fish"]
#
# # 인덱스로 접근
# print(animals[1])
# print(animals[2])
#
# # 음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동) - 최신글부터 조회
# print(animals[-1])
# print(animals[-2])
#
# # len
# print(len(animals))
#
# # append
# animals.append("hamster")
# print(len(animals))
# print(animals)
#
# animals.append('cat')
# print(animals)
#
# # insert
# animals.insert(1,'dog')
# print(animals)
#
# # remove
# animals.remove('fish')
# print(animals)
#
# #del
# # del(animals[1])
# del animals[1]
# print(animals)
#
# #clear
# # animals.clear()
# # print(animals)
#
# # index()
# print(animals.index("bird"))
# # print(animals.index("tiger"))
#
# # 수정
# index = animals.index("bird")
# animals[index] = 'lion'
# print(animals)
#
# # 그 외
# animals = ["dog", "cat", "bird", "fish"]
# print(animals * 2) #안에 있는 요소가 한번 더 들어감
#
# print("dog" in animals)
# print("tiger" in animals)
#
for animal in animals:
    print(animal)

# 실습




# # 1~90까지 list에 담고 출력
# numbers = list(range(1,91,1))
# print(numbers)
#
# number_list = [0]*90
# for i in range(len(number_list)):
#     number_list[i] = i+1
#
# number_list = []
# for i in range(len(number_list)):
#     for i in range(90):
#         number_list.append(i+1)
#
#
# #1~100까지 중 짝수만 list에 담고 출력
# odd_numbers = list(range(0,101,2))
# print(odd_numbers)
#
# odd_numbers = [0] * 50
# for i in range(len(odd_numbers)):
#     odd_numbers[i] = (i + 1) * 2
# print(odd_numbers)
#
#
# # 1~10까지 list에 담은 후 짝수만 출력
# numbers = list(range(0,11,1))
# for number in numbers:
#     int(number)
#     if number % 2 == 0:
#         print(number)
#
# number_list = []
# for i in range(10):
#     number_list.append(i+1)
#
# even_list = []
# for i in range(len(number_list)):
#     if number_list[i]%2 == 0:
#         even_list.append((number_list[i]))
# print(even_list)
#
# # 4명의 회원 정보 list에 담은 뒤 두번째 회원 이름을 변경하고 마지막 회원은 삭제
# # 4명의 회원정보를 담을 list생성
# members = [""]*4
# # 4명의 이름 입력 받은 후 데이터 나누기
# members= input("회원 이름을 입력하세요.\n")
# member = members.split(',')
# # 2번쨰 이름을 변경 할 값 입력 받기
# member[1] = input('이름을 다시 입력하세요\n')
# # 값 삭제하기
# del member[-1]
# #출력
# print(member)
#
# names = ['한동석','홍길동','이순신','장보고']
# names[1] = '서경덕'
# names.remove(names[-1])
# del names[3]
#
#


#"189,000원"을 189000으로 변경, 제너레이터 사용
# 0부터 9사이에 값이 아니면 제외
# s = "189,000 원"
# print("".join( for i in s if '0'<=i<='9'))
#

# list 안에 list
number_list = [[1, 3, 5], [2, 4, 6]]
# print(number_list[0][0])
length = len(number_list) * len(number_list[0])
# for i in range(length):
#     print(number_list[i//3][i % 3])
for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])




