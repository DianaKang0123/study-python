# 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경
# lower
fruits = ['aPPle', 'BananA', 'meLON']
lower_list = list(map(lambda x: x.lower(), fruits))
print(lower_list)

# 입력 받은 한글을 정수로 변경
# 입력 예: 삼오일구
# 출력 예: 3519
letter = input('숫자를 한글로 입력: ')
letters = "공일이삼사오육칠팔구"
print(int("".join(map(lambda x: str(letters.index(x)), letter))))


# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구
number = input('숫자 입력: ')
print("".join(list(map(lambda s: letters[int(s)], str(number)))))
# print("".join(list(map(lambda s: letters[ord(s) - 48], str(number)))))


# 리스트 경로 중 회원 서비스가 아닌 경로만 추출
urls= ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']
# 1. 서비스명(user, post, order)으로 변경(map)
# url=list(map(lambda url : url.split('/')[0],urls))
url = list(map(lambda url: url[:url.index('/')], urls))
print(url)
# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
not_user= list(filter(lambda x : x != 'user',url))
print(not_user)
