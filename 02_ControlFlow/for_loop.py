# for_loop.py
# 반복문(for)


for i in range(1, 6):
    print(i)  # print()는 기본적으로 줄바꿈하여 출력함
# 출력결과
# 1 2 3 4 5(전부 줄바꿈 하지만 가독성을위해 임의로 띄어쓰기 함)


# 줄바꿈을 안하고 싶다면 ?
for i in range(1, 6):
    print(i, end=', ') # end에 작성된 값을 줄바꿈 대신하여 출력함 즉, 출력결과는?
# 출력결과
# 1, 2, 3, 4, 5


# 리스트 순회하기
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")
# 출력결과
# apple banana cherry


text = "Hello"
for char in text:
    print(char, end=" ")
# 출력결과
# H e l l o