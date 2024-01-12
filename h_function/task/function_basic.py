'''
문제 1
파이썬 함수
*args,**kwargs 사용
회원의 주문금액(pay)과 회원의 쿠폰 할인율과 개수(coupon,count)를 전달 받은 뒤
회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
할인율이 적용된 주문 금액이 정수로 리턴된다.
쿠폰의 할인율은 백분율로 되어있다.
쿠폰의 개수는 주문 개수보다 많을 수 있다.
comprehension을 사용한다.
쿠폰 종류는 단 1개, 쿠폰 할인율은 40과 같은 1~100사이의 정수

coupon=40
count=5

아래와 같이 무조건 1개 종류의 쿠폰 여러 장이다.
40%쿠폰 5개

아래와 같은 상황은 없다.
10%쿠폰 1개, 20%쿠폰 2개
'''

# 함수의 선언
def discount(*args, **kwargs):
    # 쿠폰의 할인율과 쿠폰의 갯수를 각각의 변수에 담아 활용할 수 있도록 함
    coupon, count = kwargs.get('coupon'), kwargs.get('count')
    # 주문 금액만큼 반복, 쿠폰의 갯수 만큼 할인율을 적용하고 주문 금액이 더 크면 남는 금액에 일반 금액 출력
    if "coupon" in kwargs:
        return [
            int(args[i] - args[i] * coupon/100) if i < count else args[i]
            for i in range(count)
        ]
    return None

def discount_sample(*args,**kwargs):                            # 금액을 튜플로, 할인율과 쿠폰갯수를 딕셔너리로 받는 함수
    if "coupon" in kwargs:                                      # key 쿠폰이 딕셔너리에 있을떄(쿠폰을 입력하였을 때)
        return [                                                # 값이 여러개인 결과이므로 리스트 구조로 리턴
            int((1-kwargs.get("coupon") * 0.01) * args[i])      # 결과값 -> 할인율을 곱한 결과를 정수로 받음 딕셔너리에 get 함수로 쿠폰의 값인 정수를 받아옴
            for i in range(kwargs.get("count")                  # 컴프리핸션, 아래 조건문의 결과만큼 i를 반복
            if kwargs.get("count") <= len(args) else len(args)) # 만약 쿠폰의 갯수가 입력한 값의 갯수보다 적을 때는 쿠폰의 갯수, 많을 때는 금액의 갯수을 return
        ]
    return None                                                 # 쿠폰이 입력되지 않은 경우에는 none 리턴

'''

만약 쿠폰 적용이 안된 금액도 리턴하고 싶다면?
range(kwargs.get("count") if kwargs.get("count") <= len(args) else len(args)) 조건문을
if i > kwargs.get("count") else???

'''

# 적용 예시
print(discount_sample(2000, 4000, 3000, 50000,10000, 20000, coupon=50, count=4))
