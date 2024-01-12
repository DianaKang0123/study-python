class Car:
    # 정적변수 (static variable)
    # 생성자가 아닌 class내에 선언된 변수는 모든 객체가 공유  한곳에서 변경하면 다른 곳에서도 동일하게 변경됨(일괄적용됨)
    wheel=4         #객제가 아닌 클래스로 접근 (car.wheel로 접근)

    def __init__(self,brand='', color='', price=0):
        self.brand = brand
        self.color = color
        self.price = price
        # 초기화를 해주면 강제로 입력 할 필요가 없다. 추후 객체에서 수정할 수 있다.

    def engine_start(self):
        print(self.brand + '시동켜짐')
    def engine_stop(self):
        print(self.brand + '시동꺼짐')

mom_car = Car('Benz','black',15000)

dad_car = Car('bmw','silver',8000)

# mom_car.engine_start()
# dad_car.engine_start()
#
# print(Car.wheel)
#
# Car.wheel = 6
#
# print(mom_car.wheel)
cars = [Car, Car] #클래스 명만 적어도 내부적으로 주소값을 할당
mom_car = cars[0]()
dad_car = cars[1]()

print(mom_car,dad_car,sep='\n')
