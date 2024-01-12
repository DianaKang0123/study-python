# try:
#     number = int(input('정수를 입력하세요.'))
# except ValueError as e:
#     print('정수만 입력해주세요')
#
# print('반드시 실행되어야하는 문장')

#
# try:
#     print(10/0)
#
# # except ZeroDivisionError as e:
#     # print(e)
# # except ZeroDivisionError:
# # except:
# except Exception:                   #Exception이 모든 오류의 부모클래스이다. except: 에는 이게 생략되어있다.
#     print('0으로 나눌 수 없습니다.')

#
# datas = [1,2,3]
# try:
#     print(datas[3])
#     print('오류가 없어요')    #  위 문장에서 오류가 발생하지 않는다면 실행된다
# except ValueError:          # 다른 에러타입을 잡아버림
#     pass
#
# except IndexError:
#     print('index를 확인해주세요')
# else:                       # try에 작성한 오류가 발생하지 않았을 떄 사용함
#     print('오류가 없어요')    # 오류가 없다면 try문 밖에 작성하면 되기때문에 굳이 사용할 필요는 없다.
# finally:
#     print('반드시 실행되어야 하는 문장')


# datas = {'A':1}
# print(datas['B'])

#
# nickname = input('닉네임:')
# if nickname == '멍청이':
#      raise RuntimeError

class BadWordError(Exception):

    def __str__(self):
        return '비속어는 사용할 수 없습니다.'


def check_badword(message):
    if '멍청이' in message:
        raise BadWordError

chat = input('채팅: ')
try:
    check_badword(chat)
except BadWordError as e:
    print(e)
