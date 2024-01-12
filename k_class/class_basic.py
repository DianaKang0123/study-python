# 동물
# 이름, 나이, 성별, 음식개수, 체력개수
# 먹기, 산책하기
class Animal:

    def __init__(self,name,age,gender,feed_count=1,life=1):
        self.name = name
        self.age = age
        self.gender= gender
        self.feed_count = feed_count
        self.life = life

    #먹기 - 음식 1소모 체력 1획득
    def eat(self):
        self.feed_count -= 1
        self.life += 1

    #걷기 - 체력 1소모 음식1획득
    def walk(self):
        self.life -= 1
        self.feed_count += 1


tiger = Animal(name='호랑이',age=5,gender='수컷')
tiger.eat()

lion = Animal(name='사자',age=6,gender='암컷')
lion.walk()

print(tiger.name,tiger.age,tiger.gender,tiger.feed_count,tiger.life,sep=',')

print(lion.name,lion.age,lion.gender,lion.feed_count,lion.life,sep=',')

# offset  = 시작값(시작주소)
