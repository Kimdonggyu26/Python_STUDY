# tuple_example.py
# 튜플

# 튜플 생성
point = (3, 4)
print("포인트:", point)

# 인덱싱
print("x좌표:", point[0])
print("y좌표:", point[1])

# 튜플 언패킹
x, y = point
print("언패킹 결과:", x, y)

# 하나의 값만 있는 튜플은 쉼표를 꼭 써야 함
single = (5,)
print("하나짜리 튜플:", single)

# 튜플은 변경 불가
# point[0] = 10  # 이 줄은 에러가 발생함!!

## 실행결과
#   포인트: (3, 4)
#   x좌표: 3
#   y좌표: 4
#   언패킹 결과: 3 4
#   하나짜리 튜플: (5,)