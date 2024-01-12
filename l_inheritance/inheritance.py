class A:
    def __init__(self,name):
        self.name = name
        print('부모생성자')
    def print_intro(self):
        print('A')

class B(A):
    def __init__(self,name,age):                # self = B
        super().__init__(name)                  # super = A
        self.age = age
        print('자식생성자')
    def add(self,number1,number2):
        return number1+number2

    def print_intro(self):
        print('B')                              # 다형성(poly?) : 이름은하나인데형태가 다양
                                                # overriding : 자식에서 같은이름으로 메소드를 선언하면 부모에 있는 메소드를 무시
        # 부모의 메소드를 그대로 사용하고자 할 때(추가사항)
        super().print_intro()
        # 이렇게되면 부모 필드의 코드에 추가하여 수정할 수 있다.
        # 자식의 메소드에서 추가할 내용을 아래에 작성

b= B('한동석',20)
print(b.name)
# 자식생성자는 무조건 부모 생성자부터 호출
b.print_intro()

