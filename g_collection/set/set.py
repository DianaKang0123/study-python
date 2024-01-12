# 중복이 없고, 순서가 없다
# 순서가 없다 - iterator? 값을 가져올 수 없다
# 값의 유무를 검사하려고 만들어짐
world_set = {"korea", "america", "japan", "china"}
# 중괄호에 값이 콤마로 묶여있으면 set
print(type(world_set))
print(len(world_set))
# print(world_set[1])
# test = list(world_set)
# print(test[0])
world_set.add("korea")
print(world_set)
# console에 나타날때는 자료구조 변경 문자열 출력의 프로세스를 거쳐 나타난다
# 리스트의 중복을 제거할 때 효과적이다.
datas = [1, 1, 2, 3, 4, 4, 5, 5, 2, 3, 1]
print(list(set(datas)))