# 람다(lambda) : 이름이 없는 함수, 일회성
# lambda 매개변수,...:리턴값
# def add(number1,number2):
#     return number1+number2
#
# lambda number1,number2 : number1+number2
# 함수가 들어가야만 하는 자리에 일회성으로 사용
# 일반함수
# def change(number):
#     return number+2
# print(list(map(change,[1,2,3,4])))
# 익명함수
# print(list(map(lambda number:number+2,[1,2,3,4])))

# 실습
# 아래의 리스트의 각 요소를 2를 곱하여 변경
datas = [2, 4, 6, 8]
print(list(map(lambda number: number*2, datas)))

#각 경로앞에 /app을 붙여준다
urls = ['/game','/news','/fasion','/ranking']
print(list(map(lambda url: '/app' + url, urls)))

# filter (function,iterator)
# 1~10까지 중 짝수만 출력
list_number = list(filter(lambda number: number %2 ==0,[i+1 for i in range(10)]))
print(list)
# 'game'서비스를 제공하는 경로찾기
urls =['/app/game', '/app/news', '/app/fasion', '/app/ranking']

game_url = list(filter(lambda url:url.split('/')[-1] == 'ranking',urls))
print(game_url)