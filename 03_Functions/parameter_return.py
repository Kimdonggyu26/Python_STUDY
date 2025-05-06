# parameter_return.py
# 함수에 매개변수 전달, 값 반환

# 두 수를 더하는 함수
def add(a, b):
    return a + b

# 함수 호출 및 결과 출력
result = add(3, 5)
print("3 + 5 =", result)
# 실행결과
# 3 + 5 = 8


# 기본값 매개변수 사용
def greet(name="친구"): # 전달받은 값 없을경우 name변수 안에 "친구" 기본값
    print("안녕하세요,", name)

# 여러 값 반환하는 함수
def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result

# 호출
greet()              # 기본값 사용
greet("동규")        # 직접 인자 전달

# 여러 값 반환 받아서 출력
sum_val, diff_val = calculate(10, 3)
print("합:", sum_val)
print("차:", diff_val)

## 실행결과
#   안녕하세요, 친구
#   안녕하세요, 동규
#   합: 13
#   차: 7