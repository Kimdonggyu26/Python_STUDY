# set_example.py
# set(집합)
## 특징!! 중복 x, 순서의 개념 x

# set 생성
fruits = {"apple", "banana", "cherry", "apple"}  # 중복된 "apple"은 한 번만 들어감
print("과일 세트:", fruits)

# 원소 추가
fruits.add("orange")
print("추가 후:", fruits)

# 원소 제거
fruits.discard("banana")
print("banana 제거 후:", fruits)

# 집합 연산
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("교집합:", a & b)
print("합집합:", a | b)
print("차집합:", a - b)

## 실행결과
#   과일 세트: {'banana', 'cherry', 'apple'}
#   추가 후: {'banana', 'cherry', 'apple', 'orange'}
#   banana 제거 후: {'cherry', 'apple', 'orange'}
#   교집합: {3, 4}
#   합집합: {1, 2, 3, 4, 5, 6}
#   차집합: {1, 2}