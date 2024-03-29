class Car:
    # static 메소드와 class 메소드의 공통점
    # 객체가 아닌 클래스로 접근해서 사용한다

    # static 메소드와 class 메소드의 차이점
    # static 메소드는  전체 객체를 대상으로 실행할 문장을 작성하는데 목적을 두지만
    # class 메소드는 위의 목적과 생성자를 Wrapping 하는 목적도 가지고 있다
    # 이 떄, cls는 클래스를 받는 매개변수이다. (cls는 객체나 생성자가 아닌 클래스 그 자체이다.)

    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    @classmethod
    def translate_to_eng(cls, brand, color, price):
        if color == '빨간색':
            color = 'red'

        return cls(brand, color, price)

# classmethod 와 staticmethod 의 공통점 = class로 직접 접근해서 사용할 수 있는 메소드이다
# 차이점 - class - 만든 생성자를 사용하지 않고, 메소드를 통해 객체화한다.

car = Car.translate_to_eng('Benz','빨간색',15000)
print(car.color)