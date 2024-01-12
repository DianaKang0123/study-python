class A:
    '''
       # 클래스 선언시 생략된 자동생성자
    @classmethod
    def __new__(cls, *args, **kwargs):      #메모리의 필드를 할당하는건 __new__(주소값 생성)
        obj = object.__new__(cls)
        return obj
    '''
    def __init__(self,data1,data2,name=''):                      # 값을 받아서 처리하는건 __init__/ 값을 입력하지 않아도 self에 new에서 받은 주소값이 자동으로 할당
        print('__init__')
        print(self)
        self.data1 = data1
        self.data2 = data2
        self.name = name

    # __new__와 __init__은 한쌍이다.
    # __init__도 생략하면 자동생성된다.

    # def print_name(self,name):
    #     print(name)
    def print_name(self):
        print(self.name)

# 적용순서 new => init
# a = A() #instance #class 이름 뒤에 () = 사용,선언은 생략되어있다.
a=A(10,20,'a')
print(a)    #a에는 주소값이 담겨있는걸 확인
# a.data1=10
# a.data2=20
print(a.data1,a.data2) #파이썬은 동적바인딩이므로 A필드에 변수를 만들떄는 그냥 입력 없으면 추가, 있으면 수정
# a.print_name('a')
a.print_name()

# b=A()
b=A(100,200,'b')
print(b)
# b.data1=100
# b.data2=200
print(b.data1,b.data2)
# b.print_name('b')
b.print_name()
