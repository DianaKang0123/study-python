import json

data = {'name':'책','price':25_000,'stock': 55} # 값의 _ 는 , 대신 사용, 콘솔에는 제외되고 출력
print(data)
# 딕셔너리는 서버간 데이터 교환에 사용됨
# 딕셔너리와 제이슨은 다르다.


# 딕셔너리를 제이슨으로 변환
# ensure_ascii => 한글을 유니코드가 아닌 원본으로 출력
# indent => 보기 좋게 바꿔주며, 전달한 값은 들려쓰기 공백 수 이다.
# json_data= json.dumps(data)
json_data= json.dumps(data,ensure_ascii=False,indent= 4) #{"name": "책", "price": 25000, "stock": 55}
print(json_data) # {"name": "\ucc45", "price": 25000, "stock": 55} 출력
# 이때 \u는 유니코드의 약자

#제이슨을 딕셔너리로 변환
data_dict = json.loads(json_data)
print(data_dict)