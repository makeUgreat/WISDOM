import json 

# json 데이터 
json_data = '''
{
    "name": "김싸피",
    "age": 28,
    "hobbies": [
        "study",
        "exercise"
    ]
}
'''

data = json.loads(json_data) #문자열을 딕셔너리로 바꿔주는 명령어
            #json.loads(): json형식의 문자열을 파싱하여 python Dict 형식으로 변환
print(data)
print(type(data))

# json 데이터에서 원하는 데이터만 가져오기

name = data.get("name")  # name 키의 value 추출
print(name)