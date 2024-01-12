# hDC0wRn8eKPVBo0tHk06
# cPpoftFULR
# https://openapi.naver.com/v1/papago/n2mt
import urllib.request
import json


client_id = "hDC0wRn8eKPVBo0tHk06"
client_secret = "cPpoftFULR"

encoding_text = urllib.parse.quote('보고싶어 사랑해')
data = f'source=ko&target=en&text={encoding_text}'
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)

# -H
request.add_header('X-Naver-Client-Id',client_id)
request.add_header('X-Naver-Client-Secret',client_secret)
response = urllib.request.urlopen(request,data=data.encode('utf-8'))
rescode = response.getcode()

if rescode == 200:
    response = json.loads(response.read().decode('utf-8'))
    # print(response)

    print(response['message']['result']['translatedText'])

#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

# 안되는 경우 보안문제