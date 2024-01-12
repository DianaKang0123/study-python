'''
[종합 실습]
은행
   예금주
   계좌번호(중복 없음)
   핸드폰번호(중복 없음)
   비밀번호
   통장잔고

신한
   입금 시 수수료 50%
국민
   출금 시 수수료 50%
카카오
   잔액조회 재산 반토막

은행은 3개를 선언한다.
모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.
'''

def check(check,*args):                                    # 각 중복검사를 하기위함  전달하는것에 따라 ACCOUNT NUMBER OR PHONE
    if check not in args:
        return check
    else:
        return False


class Bank:
    total_count = 3             # 은행의 갯수
    banks = []    # 은행의 종류 판별, 2차원 리스트? 계좌의 갯수저장? 각 방에 리스트를 담아주면?

    def __init__(self,**kwargs):
        self.name = kwargs.get('name')
        self.account = kwargs.get('account')
        self.phone = kwargs.get('phone')
        self.pw = kwargs.get('pw')
        self.money = 0

    @classmethod                    #사용자가 선택한 은행에 따른 객체 생성
    def open_account(cls,bank,**kwargs):
        cls.banks = bank
        return bank,kwargs

    @staticmethod
    def check_account_number(self, account):
        check(account)

    @staticmethod
    def check_phone(self,phone):
        check(phone)                       #중복검사

    def deposit(self, amount):
        self.money += amount
        return self.money

    def withdrow(self, amount):
        if self.money >= amount:
            self.money -= amount
            return self.money

    def balance(self):
        return self.money

    def __str__(self):
            return f'name: {self.name}'


class Shinhan(Bank):
    def deposit(self, amount):
        self.money += (amount * 0.5)

class Kookmin(Bank):
    def withdraw(self, amount):
        super().withdrow(amount)
        self.money -= (amount * 1.5)

class KaKao(Bank):
    def balence(self):
        return self.money * 0.5



if __name__ == '__main__':

    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"



    while True:
        name = input(owner_message)
        account = input(account_number_message)
        phone = input(phone_message)
        pw = input(password_message)
        money = input(money_message)
        deposit = int(input(deposit_message))
        withdraw = input(withdraw_message)
        bank_choice = input(bank_menu)
        if bank_choice == "1":
            while True:
                menu_choice = input(menu)
                if menu_choice == "1":
                    Bank.open_account(bank=bank_choice,name=name,account=account,phone=phone,pw = pw,money=money)
                if menu_choice == "2":
                    pass
        elif bank_choice == "2":
            pass
        elif bank_choice == "3":
            pass




