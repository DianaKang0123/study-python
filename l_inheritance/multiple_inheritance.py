# 다중 상속
# 파이썬은 다중상속을 지원한다
# 하지만 여러 부모를 상속 받았을 때 동일한 이름의 필드가 겹치면
# 자식에서 사용 시 혼란을 야기한다
# 이때 mro()를 사용하여 접근 순서를 확인 할 수 있으나
# 자식에서 재정의한 뒤 사용하는 것이 오히려 낫다
# 다주상속은 다양한 모호성을 발생시키기 때문에 되도록 피하는 것이 좋다.

class A:
    pass


class B(A):
    def print_info(self):
        print('B')


class C(A):
    def print_info(self):
        print('C')


class D(B,C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)

# 이 경우 b와c에 동일한 이름의 필드에 접근 시 어떤 부모의 필드인지 모름
# 우선순위는 상속 작성 순서
print(D.mro())                                                  #mro -> 동작순서 확인 함수
D().print_info()
