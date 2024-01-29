from crud_module import *
import hashlib
from task_message_module import *
import json
import o_api.external.sms.message as message
import random

# 회원가입(sms api) - 랜덤한 인증번호 6자리 발송후 검사

# 아이디(이메일) 중복검사

if __name__ == '__main__':
    random_number = str(random.randint(100000,999999))
    print(random_number)

    while True:
        # 이름과 전화번호 입력받기
        input_name = input(name)
        input_phone = input(phone)
        # 입력한 전화번호 sms 발송
        data = {
            'messages': [
                {
                    'to': input_phone,
                    'from': '01048496691',
                    'text': f'{input_name} 님의 인증 번호는 {random_number} 입니다.'
                },
            ]
        }
        res = message.send_many(data)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))

        check_number = input(certifi_number)

        if random_number == check_number:
            input_email = input(email)
            find_by_id_query = "select email, password, name from tbl_user where email = %s"
            params = [input_email]
            member = find_by_id(find_by_id_query, params)

            if member is not None:
                print('이미 사용중인 아이디 입니다.')
                continue

            else:
                input_password = input(password)
                insert_query = "insert into tbl_user(email, password, name, phone) \
                                values (%s, %s, %s, %s) "
                # 암호화
                seal_password = input_password
                encryption = hashlib.sha256()
                encryption.update(seal_password.encode('utf-8'))
                insert_params = [input_email, encryption.hexdigest(),input_name,input_phone]
                save(insert_query, insert_params)

            print('가입이 완료되었습니다.')

            # 로그인 - 마이페이지로 이동(회원의 정보를 전부 출력 print) - 비밀번호 변경
            # 회원 비밀번호 변경 (email api) 랜덤한 코드 10자리 발송 후 검사 -> input-> y/n
#










# # 회원 정보 전체 조회
# find_all_query = "select email, password, name from tbl_member"
# # members = find_all(find_all_query)
# # print(members)
#
# # 이메일로 회원 1명 조회
# find_by_id_query = "select email, password, name from tbl_member where email = %s"
# params = ['lss1234@naver.com']
# # member = find_by_id(find_by_id_query, params)
# # print(member)
#



# 로그인 - 마이페이지로 이동(회원의 정보를 전부 출력 print) - 비밀번호 변경
# 회원 비밀번호 변경 (email api) 랜덤한 코드 10자리 발송 후 검사 -> input-> y/n

# 사용자가 입력한 문장을 영어로 번역, 한국어와 번역된 문장을 DBMS에 저장
# 번역 내역을 전체 조회

# 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)
# 이미지 경로 :
# 전체 경로와 추출한 텍스트 조회(전체 조회)