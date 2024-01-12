# 전역 변수(global variable)
# 어떤 지역 밖에 선언된 변수

# 여러 함수에서 공유해야 하는 값이 있을 경우 사용

# 지역 변수(local variable) : 선언이 한 구역 안에서 이루어지면 그 선언은 해당 구역 안에서만 사용가능
# 어떤 지역 안에 선언 된 변수

count = 0 # 전역변수

def increase():

    # print(count)
    # count = 0 # 지역 변수 - 위에 있는 count와는 다름 , pvm이 서로 다른곳에 저장
    # 밖에 있는 전역 변수를 수정하고 싶을 떄는 앞에 global 키워드를 사용
    global count
    count += 1

increase()
print(count)