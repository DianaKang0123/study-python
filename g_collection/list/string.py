# # print(list('ABC'))
# for i in "ABC":
#     print(i)
#
# # upper(), lower()
# print("Apple123!@#".upper())
# print("Apple123!@#".lower())
#
# # split()
# # maxsplit( 여기까지만 분할하고 나머지는 하나의 값으로 해라)
#
# data = "사과, 바나나, 파인애플, 포도, 복숭아"
# print(data.split(", ", maxsplit=2))
#
# print("A B C D E F G H I J K".split())
# print("A      \n        B".split())
# # 공백 및 제어문자도 구분점으로 인식
# print("A     B".split(" "))
#
# # join()
# # 현재시간을 알맞은 형식으로 바꿀 떄 사용
# # 리스트 안의 여러요소를 원하는 구분점으로 연결
# print(":".join(["a","b","c"]))
# print("".join(["a","b","c"]))
#
# # replace('기존값, '새로운값)
# print("A b C d".replace(" ",""))
# print("안녕! 반가워!".replace("!","?"))
#
# # strip(), lstrip(), rstrip() - 앞 뒤의 공백 제거할 때 보통 사용한다.
# print("a     b      c       ".strip())
# print("a     b      c       ".strip(" "))
# print("apple".strip("p")) # 중간값은 사라지지 않음
# print("apple".strip("a")) # 맨 앞인 a는 사라짐
#
# # index(찾는값) # 찾고자 하는 값이 없으면 오류가 발생, 반드시 포함되어야 하는 값에 사용
# print("ABC".index("A"))
# # print("ABC".index("Z")  # 오류 /
#
# # find(찾는값)  # 찾고자 하는 값이 없으면 -1을 가져온다
# print("ABC".find("A"))
# print("ABC".find("Z"))
#
# # in: 값의 유무 검사
# print("ABC" in "Z")

# # count() : 전달한 값이 몇개가 있는지 검사
# #"189,000원"을 189000으로 변경, 제너레이터 사용
# # 0부터 9사이에 값이 아니면 제외
s = "180,000 원"
# for i in s:
#     if '0'<= i <= '9': # 조건식에서 '0' 을 입력하면 자동으로 정수로 바뀜, i가 문자열이기 때문에 '0','9'도 맞춰야함(아스키코드)
#         print(i)
# print([i for i in s if "0" <= i <= "9"])
# print("".join(i for i in s if "0" <= i <= "9"))

string="가나다라마바사"
letter = "아"

print(string.find(letter))