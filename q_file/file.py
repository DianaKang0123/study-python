# 절대 경로 : 대한민국 서울시 강남구 역삼동 123-123 101동 122호
# 경로를 처음부터 작성하는것
# 어떤 위치에 있든 상관없이 찾아갈 수 있는 경로
# C:/user/dianakang/...
# 맥이나 리눅스는 /로 시작


# 상대 경로 : 직진해서 좌회전 후 오른쪽 건물
# 내가 있는 위치를 기준으로 작성
# 현재 위치에 따라 변경되는 경로
# ./ ->  현재경로
# ../ -> 이전경로(뒤로가기)
# ./src/iamges, ../../a/b/ , src/iamges(./ 생략)

# 파일 생성하기
#
# file = open('food.txt','w',encoding='UTF-8') # 없으면 새로 만들어서 가져오고, 있으면 그대로 가져옴
# file.write('부대찌개\n')      # 내용작성후 열려있는상태, 파이썬은 자동으로 flush
# file.write('햄버거\n')
# file.close()                # 반드시 닫아주어야한다.
# # 여러번 실행해도 라인이 추가되지 않음-> open을 w로 하는 순간 파일 안에 내용이 다 삭제된다.

# #내용 추가하기
# file = open('food.txt','a',encoding='UTF-8')
# file.write('피자\n')
# file.close()

# # 파일 읽기
# try:
#     file= open("food.txt",'r',encoding='UTF-8')
#     # print(file.readlines())       #lines를 쓰는 경우 반복문으로 값을 가져오면 되고
#     # for i in range(5):
#     #     print(file.readline(), end='')
#
#     # readline => 반복문 값이 더 많으면 빈 문자열을 반환함
#
#     line=None                      # line을 쓰면 아래와 같이 써주면 된다.
#     while line != '':
#         line = file.readline()
#         print(line, end ='')
#
# except FileNotFoundError:
#     print('경로를 다시 확인해 주세요')

# # with를 사용하면 자동으로 file이 close 된다.
# with open('food.txt','r',encoding='utf-8') as file:     #객체를 만들고 뒤에 담아줌, 파일이 자동으로 close를 함
#     print(file.readlines())                             # with 는 클래스에서 enter와 exit가 자동 실행됨

# 수정
# 외부 파일에 있는 내용을 담아줄 변수 선언
content= ''


with open('food.txt','r',encoding='utf') as file:
    line = None
    # 전체 내용을 한 줄 씩 읽어오기
    while line != '':
        # 한줄을 line 에 담기
        line = file.readline()
        #  담은 내용이 찾고있는 햄버거일 경우
        if line == '햄버거\n':
            # 치킨으로 변경후 담아줌
            content += '치킨\n'
            # 치킨으로 변경 한 값외 다른 값이 변경되지 않게 break로 while 문 탈출
            continue
        # 수정 대상이 아닌 줄은 그대로 content에 담기
        content += line
        # 수정 완료된 문자열 값 확인
        print(content)

# 기존의 내용을 수정 완료된 문자열로 덮어쓰기
with open('food.txt','w',encoding='utf-8') as file:
    file.write(content)

# 원본파일에 덮어쓴 내용 확인*

with open('food.txt','r',encoding='utf-8') as file:
    print("".join(file.readlines()))