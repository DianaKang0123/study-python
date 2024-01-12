# mutable : 변할 수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10
print(data_list2)
print(data_list1)
# list1은 따로 변하지 않았음에도 값의 변화가 반영되어있다.
# list를 쓸 떄는 원본을 수정하면 안됨
# 실무에서 사용 지양
# 리스트는 제한을 줄 수 없음
# len 함수로 제한을 줘야함
# immutable : 변할 수 없는
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1
# tuple은 한번 넣으면 수정을 할 수 없다.
# tuple의 값을 수정하고싶을때
# test = list(data_tuple2)
# test[0] = 10
# print(test)
data_tuple2=data_tuple1 + (5,6)
# 이경우 연결된 새로운 tuple이 만들어 진 것
#  원본은 유지됨
print(data_tuple2)
print(data_tuple1)
# 소괄호가 없어도 tuple
datas= 1,2
print(type(datas))
#구분되는 코드값 ex) 404, 505
ERROR_CODE = 1,
# 값이 하나여도 뒤에 ,를 찍으면  TUPLE
print(type(ERROR_CODE))
# 대문자 변수는 변경할 수 없는 것(상수)을 나타냄
# tuple 은 함수에서 많이 사용됨 - 값이 변하지 않아야하므로