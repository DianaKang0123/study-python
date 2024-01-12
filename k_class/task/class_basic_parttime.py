# PartTimer

# '모든 직원'에 공통적으로 적용되는 내용
# - 시급
# - 직원수

# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)

# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리

class PartTimer:
    pay_of_hour = 10000
    total_of_part_timers = 0

    def __init__(self, nickname, place='청담동'):
        self.nickname = nickname
        self.place = place
        self.total_pay = 0
        PartTimer.total_of_part_timers += 1

    def calculate_money(self,hour,bonus=0):
        total_money = (hour * PartTimer.pay_of_hour) + bonus
        self.total_pay += total_money

parttimers = [PartTimer,PartTimer,PartTimer,PartTimer]

ryan= parttimers[0]('라이언')
neo= parttimers[1]('네오')
print(ryan.total_pay,ryan.nickname,ryan.place)
result = ryan.calculate_money(8,6000)
print(ryan.total_pay,ryan.nickname,ryan.place)
