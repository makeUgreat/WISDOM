import requests

url = "https://fakestoreapi.com/carts"  # 요청을 보내는 서버의 주소
response = requests.get(url).json()  #requests.get(url) 해당 서버에 데이터를 달라고 요청을 보내는 함수
                                    #.json() 내부의 데이터를 JSON(딕셔너리와 비슷) 형태로 변환해주는 함수
print(response)