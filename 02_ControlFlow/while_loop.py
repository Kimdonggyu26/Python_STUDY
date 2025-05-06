# while_loop.py
# 반복문(while)

i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
# 출력결과
# 1 2 3 4 5


while True: # 무한루프 설정정
    num = int(input("Enter a number: "))
    if num == 0:
        print("Stopped!")
        break # 반복 종료
    print("You entered:", num)
# 출력결과
#   사용자가 0을 입력할때까지(break를 만날때까지) 반복문은 지속된다.


i = 1
while i <= 3:
    print("Counting:", i)
    i += 1
else: # while 조건에 부합하지 않을경우 else로 이동
    print("Done!")
# 출력결과
#   Counting: 1
#   Counting: 2
#   Counting: 3
#   Done!