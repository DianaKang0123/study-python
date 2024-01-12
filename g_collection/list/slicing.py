# #인덱스 슬라이싱
# animals = ['dog','dog','cat','bird','fish']
#
# # list[inclusive start = 0 : exclusive_end=len(list)] ->list
# print(animals[0])
# print(animals[0:3])
# print(animals[1:4])
# print(animals[:2])
# print(animals[2:])
# # list[inclusive start = 0 : exclusive_end=len(list):step = 1] ->list
# # step은 메모리 소모가 크므로 잘 쓰지 않음
# foods=['noodle','meat','bread','chicken']
# print(foods[:3:2])
# print(foods[2::2])
#
# #역순 출력
# print(foods[::-1]) # 기존 순서와 반대로 출력됨

number_list= list(range(1,11))
print(number_list)

#1,3,5,7,9
#6,5,4,3,2
#2,4,6
#2,3,4,5,6,7
#
print(number_list[::2])
print(number_list[5:0:-1])
print(number_list[1:6:2])
print(number_list[1:7:])

animals = ['dog', 'dog', 'cat', 'bird']
zoo = ['panda', 'giraffe']

# 기존 값은 사라지고 zoo list 안에 있는 요소가 각각 들어간다.
animals[1:2] = zoo
print(animals)

# 기존 값은 뒤로 밀리고 해당 자리에 값이 들어간다.
animals.insert(animals.index('dog') + 1, 'giraffe')
print(animals)

# 기존 값은 뒤로 밀리고 zoo list 통채로 들어간다.
animals.insert(animals.index('dog') + 1, zoo)
print(animals)

# 슬라이싱, insert, del 를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog', 'whale', 'bird']

animals = ['dog', 'dog', 'cat', 'bird']
zoo = ['hamster','fish']
animals[1:1] = zoo
animals.insert(animals.index('bird')-1,'whale')
del animals[animals.index('cat')]
print(animals)

