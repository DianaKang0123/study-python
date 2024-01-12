# 1~15까지 출력
for i in range(15):
    print(i + 1)

# 30~1까지 출력
for i in range(30):
    print(30 - i)

# 1~100까지 중에 홀수만 출력
for i in range(50):
        print(i * 2 + 1)

# 1~10까지 합 출력
sum = 0
for i in range(10):
    # i+=1
    # sum = sum + i
    sum += i+1
print(sum)


# 1~n까지 합 출력
message1 = "숫자를 입력하세요.\n"
message2 = 'n: '
number = int(input(message1 + '\n'+message2))
sum=0
for i in range(number):
    sum += i+1
print(sum)

# 3 4 5 6 3 4 5 6 3 4 5 6 출력
# a % n = 0~n-1
for i in range(12):
    i = i % 4 + 3
    print(i,end=" ")

# 1,235,500 dmf 1235500으로 출력한다.
data = '1,235,500'
result = ''
for i in data:
    if i != ',':
        result += i
result = int(result)
print(result)

#1부터 10까지 중 3까지만 출력
# break 활용
for i in range(10):
    print(i+1)
    if i == 2:
        break
#print의 위치 중요
# break는 조건식과 써야함

#1~10 중 4 제외 출력
for i in range(10):
    if i == 3:
        continue  #밑의 문장을 하지 않을 때 사용, 항상 아래에 코드가 있어야함
    print(i+1)





