# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""
# read = 전체 문자열 값을 다 가져옴
# contents = ''
# result = []
# with open('./alicetest.txt','r',encoding='utf-8') as file:
#     line = None
#     while line != '':
#         for line in file.readlines():
#             contents = line.split()
#             for content in contents:
#                 lower_content = content.lower()
#                 if lower_content.isalpha() == True:
#                     if len(lower_content) > 2:
#                         lower_content

#
# with open('./alice.txt','r',encoding='utf-8') as file:
#     line = file.read()
#     words = line.split()
#     word_dict = {}
#     for word in words:
#         word = word.lower()
#         if word.isalpha() is True:
#             word_dict[word] = word_dict.get(word,0) + 1
# for word in word_dict.keys:
#     if word_dict[word] >= 100:
#         print(word_dict)
# # for word in keys:
# #     result = word + ':' + str(word_dict[word])
#
# print(word_dict)


# ----------------------------------------------------------------------------------

with open('alice.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()

temp = ""
for character in content:
    if 'a' <= character <= 'z':
        temp += character
        continue
    temp += " "

content = temp

words = [
    word
    for word in content.split()
    if len(word) > 1
]

result = {}
for word in words:
    if result.get(word) is not None:
        result[word] += 1

    else:
        result[word] = 1

result = {
    word: result[word]
    for word in result
    if result[word] >= 100
}               # 딕셔너리도 컴프리핸션이 가능하다

sorted_key = sorted(result, key=result.get, reverse=True)
# key에 함수를 전달하면 리스트의 각 값에 함수를 입려 나온 값을 기준으로 정렬됨
# 이때 값이 아닌 원래 리스트의 요소가 정렬됨
for key in sorted_key:
    print(key, result[key])

#
#
#
# def change(data):
#     return data * -1
#
# datas = [1, 2, 3, 4]
#
# print(sorted(datas, key=change))

# print(list({"A": 1, "B": 2, "C": 3}))