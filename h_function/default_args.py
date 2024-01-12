# 만약 값을 매개 변수로 전달하지 않았을 경우
# 기본값을 설정 할 수 있고, arg=value로 작성한다.

def sub(number1,number2,number3,number4=0):
    return number1-number2-number3-number4

result = sub(1,2,3)
print(result)

#실습
#이름을 전달받지 못하면 익명
#나이를 전달받지 못하면 0

def get_info(name='익명', age=0): # if age(값이 반드시 있는경우) 는 age를 앞에 써야한다
    return f'이름:{name},나이:{age}'


print(get_info(name="한동석"))
print(get_info(age=20))

