# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.

message = '이메일: \n'
emailid, domain = input(message).split('@')

formatting=f'아이디: {emailid}\n도메인: {domain}'

print(formatting)


'''
    첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력 받아서
    각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째 자리 까지 출력한다.

    1yd: 91.44cm
    1in: 2.54cm

    예)
        yard 입력: 10
        inch 입력: 10

        10 yard는 914.4cm
        10 inch는 25.4cm
'''
yard_message='yard, inch 변환기\nyard 입력: '
inch_message='inch 입력: '
yard =float(input(yard_message))
inch =float(input(inch_message))

yard_result=round(yard*91.44,2)
inch_result=round(inch*2.54,2)

formatting=f'\n{yard}yard는 {yard_result}cm\n{inch}inch는 {inch_result}cm'

print(formatting)

'''
yard, inch 변환기
yard 입력: 10
inch 입력: 10

10.0yard는 914cm
10.0inch는 25.4cm

10.0을 10으로 변경하기 위해서는 int
'''