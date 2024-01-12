# 정렬
number_list = [5,4,6,1,3]

# 1. sort() - 원본을 변경하게 된다
# number_list.sort(reverse=True)
# print(number_list)

# # 2. sorted() : 원본은 유지되고 새로운 리스트가 만들어진다.
sorted_list = sorted(number_list, reverse=True)
print(number_list)
print(sorted_list)
