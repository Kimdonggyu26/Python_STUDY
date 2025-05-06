# list_example.py
# 리스트 예제

# 리스트 생성
fruits = ['apple', 'banana', 'cherry']
print("리스트:", fruits)

# 인덱싱
print("첫 번째 과일:", fruits[0])

# 슬라이싱
print("두 개의 과일:", fruits[0:2]) ##[여기부터:여기전까지] "여기전까지"가 없다면? "끝까지"

# 리스트에 항목 추가
fruits.append('orange')
print("추가 후:", fruits)

# 리스트에서 항목 제거
fruits.remove('banana')
print("제거 후:", fruits)

# 리스트 반복
for fruit in fruits:
    print("과일:", fruit)

## 출력결과
#   리스트: ['apple', 'banana', 'cherry']
#   첫 번째 과일: apple
#   두 개의 과일: ['apple', 'banana']
#   추가 후: ['apple', 'banana', 'cherry', 'orange']
#   제거 후: ['apple', 'cherry', 'orange']
#   과일: apple
#   과일: cherry
#   과일: orange