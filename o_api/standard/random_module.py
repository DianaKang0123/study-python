import random as r




#randint(시작값, 끝값)
# print(r.randint(1,10)) # start, end (시작값과 끝값이 포함되어있다.) 중 랜덤한 값이 나온다

# 확률
# 1. list 선언(리스크의 칸에 따라서 확률의 단위가 다라짐(10칸은 10단위 100칸은 1단위))
unit = 10
unit_dict = {1:100,10:10}
rating = [0] * unit_dict
확률 = 30
# 2. 확률을 계산해서 해당 자리에 1 대입
for i in range(확률//10):
    rating[i] = 1

# 10개 중 1은 3개 있기 떄문에 1이 나올 확률은 30% 이다.
if rating[r.randint(0, len(rating)-1)] == 1:
# -1 => 인덱스는 길이 -1 : 인덱스는 0 으로 시작
    print('강화 성공')
else:
    print('강화 실패')

