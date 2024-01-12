
class Magic:
    def __str__(self):
        return f'{self.__repr__()}, __repr__() 사용됨.'

# 객체를 출력하면 항상 __repr__()가 자동으로 뒤에 붙는다.
# print(Magic().__repr__())
# 만약 해당 클래스에서 __str__()을 재정의했다면, __repr__()가 아닌 __str__()이 사용된다.
# print(Magic().__str__())
# 따라서, 생략해서 작성하면 __str__()이 붙게된다.
print(Magic())


'''
class Magic:

    def __init__(self,name):
        self.name = name
    
    # 초기화된 필드를 확인하고자 할 떄 사용된다.
    def __str__(self):
        return f'name : {self.name}'

magic = Magic('magic')
print(magic)
'''
class Student:
    def __init__(self,number, score):
        self.number = number
        self.score = score

    def __add__(self, other):                   # other = 객체
        return self.score + other.score

    def __eq__(self,other):

        # 주소비교
        if self.__repr__() == other.__repr__(): #__repr__를 따로 재정의 해주지 않으므로 주소값을 비교하기 위해
            return True

        # 타입비교
        # isinstance(객체 , 타입): 전달한 객체가 전달한 타입일 경우 True 아니면 False
        if isinstance(other,Student):           # 앞 객체가 뒤에 있는 타입인지 검사
            # 값 비교
            return self.number == other.number

        return False

std1=  Student(1,30)
std2= Student(1,50)     # 주소값 다름 __eq__의 두번쨰 조건으로 검사
# std2= std1                        # 주소값 공유 __eq__의 첫번째 조건 true
# std1+std2 => 안됨
# total = std1.__add__(std2)         #= 재정의한 __add__를 통해서 std1.score + sed2.score
print(std1+std2)            # 데이터에 전달한 재정의한 메소드는 연산자로도 사용가능하다
# print(total)                # 데이터 전달에 용이함
print([1,2,3].__getitem__(2))
print([1,2,3].__contains__(2))      # 재정의를 할떄 사용!
print(std1==std2)