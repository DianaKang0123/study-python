import datetime

# 저장 되는 형식과 화면에 뿌리는 형식이 다르다.
# 콘솔에 나오는 값은 저장되는 방식

# 현재날짜 - 무언가를 새롭게 등록할 때 (like 회원가입시 가입일자)
now = datetime.date.today()
time = datetime.datetime.now()
print(now)
print(time)

print(now.year, now.month, now.day, sep='/')
print(time.hour, time.minute, time.second, sep=':')

# 지정 날짜 - 이미 저장된 날짜를 가져와서 date type으로 바꿀 때
date = datetime.datetime(2024, 1, 1, 12, 0, 0)
print(date)

