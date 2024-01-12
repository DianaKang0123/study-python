# https://ocr.space/OCRAPI
# K85476724888957

#https://api.ocr.space/parse/imageurl?apikey=``&url=``
#https://api.ocr.space/parse/imageurl?apikey=``&url=``&language=``&isOverlayRequired=true
import requests
# no module 오류시 해당 모듈이름에 마우스를 대면 밑에 install이 나옴, 바로 설치해주면됨
url= 'https://api.ocr.space/parse/imageurl?apikey=K85476724888957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true'
response = requests.get(url) #  requests = 요청 / .get => 요청방법(like 브라우저의 검색창
response.raise_for_status()

result = response.json() # 요청의 결과값
print(type(result))
print(result['ParsedResults'][0]['ParsedText'])
