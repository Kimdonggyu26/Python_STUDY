# variables_and_types.py
# 변수 선언과 자료형


# 변수 선언
name = "Python"
version = 3.13
is_dynamic = True

## 파이썬은 변수 선언 시 자료형을 따로 지정하지 않아도 자동으로 판단한다.
print("언어:", name)
print("버전:", version)
print("동적 타입 언어인가?", is_dynamic)
print("name의 자료형:", type(name))
print("version의 자료형:", type(version))
print("is_dynamic의 자료형:", type(is_dynamic))

# 출력결과
#  언어: Python
#  버전: 3.13
#  동적 타입 언어인가요? True
#  name의 자료형: <class 'str'>
#  version의 자료형: <class 'float'>
#  is_dynamic의 자료형: <class 'bool'>