# dictionary_example.py
# dict
## 특징 ! key, value의 형태로 데이터를 저장하는 자료형

# 딕셔너리 생성
person = {
    "name": "김동규",
    "age": 27,
    "city": "서울"
}
print("기본 정보:", person)

# 값 접근
print("이름:", person["name"])

# 값 수정
person["age"] = 26
print("수정된 나이:", person["age"])

# 새 항목 추가
person["job"] = "Developer"
print("추가된 직업:", person)

# 항목 삭제
del person["city"]
print("도시 삭제 후:", person)

# 반복
print("딕셔너리 전체 출력:")
for key, value in person.items():
    print(f"{key}: {value}")


## 실행결과
#   기본 정보: {'name': '김동규', 'age': 27, 'city': '서울'}
#   이름: 김동규
#   수정된 나이: 26
#   추가된 직업: {'name': '김동규', 'age': 26, 'city': '서울', 'job': 'Developer'}
#   도시 삭제 후: {'name': '김동규', 'age': 26, 'job': 'Developer'}
#   딕셔너리 전체 출력:
#   name: 김동규
#   age: 26
#   job: Developer