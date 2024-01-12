# 캐릭터 닉네임을 정할 떄 비속어를 사용하지 못하게 막아주기
# 바보 멍게 해삼 운영자
# 직접 에러 제작
# 발생 시 안내 메세지 출력하기


# 닉네임 오류 클래스를 만들어 출력 문구 지정하기
# 부모 클래스는 오류 클래스인 Exception
class NickNameError(Exception):
    # 출력 오류 문구 재정의 __repr__대신 출력하는 문구
    def __str__(self):
        # 콘솔에 실제로 출력되는 문구
        return 'NickNameError-비속어를 사용할 수 없습니다.'

# 비속어의 수정이 있을 수 있으므로 리스트에 담아주기
badwords = ['바보', '멍게', '해삼', '운영자']

# 함수를 이용하여 사용을 용이하게만듬
#nickname은 사용자가 실제로 입력하는 nickname
def check_nickname(nickname):

    # 비속어 리스트에서 비속어를 반복문에 담아줌
    for badword in badwords:
        # 담아진 각각의 비속어가 닉네임 안에 있니?
        if badword in nickname:
            # 있다면 닉네임 오류를 발생 시켜
            raise NickNameError

# 실제 사용: 사용자가 입력하는 닉네임을 nickname으로 선언
nickname = input('닉네임: ')

#오류 검사
try:
    # 함수에 사용자가 입력한 닉네임을 받아서 검사
    check_nickname(nickname)
    print(f'어서오세요 {nickname}님')
# NicknameError 발생시 클래스의 return값 실행
except NickNameError as e:
    # return 값을 콘솔에 프린트해줌
    print(e)