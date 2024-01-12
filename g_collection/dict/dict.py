# 딕셔너리 선언
student= {
    'name':'한동석',
    'email':'tedhan1204@gmail.com'
}
# 딕셔너리의 ket인 name 으로 value 출력
print(student['name'])
# 딕셔너리의 .get('key') 함수를 사용하여 value 출력
print(student.get('name'))

# get()를 사용하면 key 값을 찾지 못하였을 떄 원하는 default값으로 설정이 가능하며,
# dafault값이 없을 떄에는 none을 가져온다
# print(student['phone']) # 없는자료 = 오류
print(student.get('phone')) # 없는자료 = none
print(student.get('phone','01048496691')) # 없는 자료의; default 값을 바로 지정 가능

# name 키값이 이미 있기 때문에 수정
student['name'] = '홍길동' # 수정
print(student)
# phone 값이 없기 떄문에 추가
student['phone'] = '01012345678'
print(student)

# if 조건문
# email 이라는 key 값이 dict student에 있다면: 있으면 True
if 'email' in student:
    # 실행문 dict student의 key가 email 인 값을 대입 연산자 뒤의 값으로 바꾸어라
    student['email'] = 'hgang6183@gmail.com' # 수정
# 조건문 if 의 값이 false라면(key 가 student 에 없다면
else: # 추가
    # key가 email인 공간을 만들고 그 곳에 value 를 넣어라
    student['email'] = 'hgd1234@gmail.com'

# 출력
print(student) #{'name': '홍길동', 'email': 'hgang6183@gmail.com', 'phone': '01012345678'}

# my_dict 딕셔너리 선언, 이차원 리스트(row안에 리스트 안에 다시 딕셔너리 타입))
my_dict = {
    1: '한동석',
    'two' : '20살',
    False : [10,20,30],
    "row" : [
        {"name":"ted",'age':40},
        {"name":"jack",'age':30},
        {"name":"john",'age':20}
    ]
}


# row 에 있는 회원 3명의 정보를 모두 출력
# if 조건문, key 'row'가 my_dict 에 있는지, 있으면 true
if 'row' in my_dict:
    # row 선언 딕셔너리의 key가 row 인 값(딕셔너리들)
    row = (my_dict["row"])
    # row 안의 딕셔너리를 info로 반복
    for info in row:
            #분리 후 info의 name 키의 값 , age 키의 값 출력
            print(f'{info["name"]}, {info["age"]}')

# 1~10까지 중 홀수와 짝수가 있다. 사용자가 짝수를 입력하면 짝수만 출력, 홀수를 입력 하면 홀수만 출력한다.
# dict사용
message = '홀수 혹은 짝수 입력 : '
number_dict = {
    "홀수": [1,3,5,7,9],
    "짝수" : [2,4,6,8,10]
}
data = input(message)
for number in number_dict[data]:
    print(number,end=', ')
number_dict = {
    "홀수": [i*2+1 for i in range(5)],
    "짝수":[(i+1)*2 for i in range(5)]
}
print(", ".join(map(str, number_dict[input('홀수 혹은 짝수: ')])))

number_dict = {
    True: [i*2+1 for i in range(5)],
    False:[(i+1)*2 for i in range(5)]
}
print(", ".join(map(str, number_dict[input('홀수 혹은 짝수: ') == '홀수'])))

student= {
    'name':'한동석',
    'email':'tedhan1204@gmail.com'
}

# key 분리
print(list(student.keys()))
# value 분리
print(list(student.values()))
# item 분리
# list안에 tuple 타입으로
print(list(student.items()))

for key,value in student.items():
    print(f'key: {key}, value: {value}')

