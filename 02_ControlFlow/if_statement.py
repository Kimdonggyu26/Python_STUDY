# if_statement.py
# 조건문
# :의 의미 ==> :는 "여기부터 블록이 시작된다"는 의미.
# C언어나 JAVA와 달리 python은 :과 들여쓰기로 블록을 구분함.

age = int(input("나이를 입력하세요: ")) # 26입력

if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")
# 출력결과
#   성인입니다.

# if_elif_else
score = int(input("점수를 입력하세요 (0~100): ")) # 85입력

if score >= 90:
    print("A학점입니다.")
elif score >= 80:
    print("B학점입니다.")
elif score >= 70:
    print("C학점입니다.")
elif score >= 60:
    print("D학점입니다.")
else:
    print("F학점입니다.")

# 출력결과
#   B학점입니다.