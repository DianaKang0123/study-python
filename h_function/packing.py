# # unpacking: 값을 풀어서 적는 것
#
# # def get_total(number1,number2,number3):
# #     return number1 + number2 + number3
#
#
# #packing : 값을 묶어서 적는 것
#
# def get_total(*numbers): #numbers의 타입은 tuple
#     # 외부에 전달받은 값들이 numbers(tuple)에 저장된다
#     print(type(numbers))
#     # numbers의 타입 확인
#     total=0
#     for number in numbers:
#         total += number
#     return total
# # 여러개의 값을 ,로 구분하여 전달한다
# # total = get_total(1,2,3,4,5)
# # print(total)
#
#
# # 여러개의 값을 하나로 묶어서 전달하게되면 packing 으로 인해 첫번째 방에 통째로 들어가게 된다.
# # 즉 결과  = ([1,2,3,4,5], )
# # 따라서 내부의 요소를 각각 전달하고 싶다면, 앞에 *를 작성해야한다.
# numbers = [1,2,3,4,5]
# total = get_total(*numbers) #numbers앞에 *이없으면 list를 하나의 값으로 취급
# print(total)

# 국어 영어 수학 점수를 전달받은 뒤 총점을 출력하는 함수
# packing 으로 제작

def total_score(name, *scores):
    print(name+'님의 총점은')
    total = 0
    for score in scores:
        total += score
    return total

print(total_score('diana', 90,80,70,70,70))



# 문자열에서 'A'가 몇개 잇는지 검사하는 함수
# packing으로 제작 하기

def inspect_A(*strs):
    return [string.count("A") for string in strs]
    # count = 0
    # counts = []
    # for str in strs:
    #     for s in str:
    #         if s =="A":
    #             count+=1
    #     counts.append(count)
    #     count = 0
    # return counts

test = "asdfsAADASD","ASDF","asdf","asdf"
result = inspect_A(*test)
print(result)
