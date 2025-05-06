# break_continue.py
# break와 continue 사용 예제
# break => 반복문을 종료한다.
# continue => 진행중인 반복문을 멈추고 다음 반복으로 넘어간다.

for i in range(1, 6):
    if i == 3:
        print("3은 패스")
        continue  # 3은 건너뛰고 다음 반복으로 넘어감
    if i == 5:
        print("5에서 종료")
        break     # 반복문 종료
    print(f"현재 숫자: {i}")
# 실행결과
#   현재 숫자: 1
#   현재 숫자: 2
#   3은 패스
#   현재 숫자: 4
#   5에서 종료