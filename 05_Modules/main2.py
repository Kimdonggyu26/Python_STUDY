# main2.py
# from 모듈명 import 함수명 << 이러한 형식으로 특정 함수만 불러오기도 가능!

from my_module import greet

print(greet("Python"))
#print(add(1, 2)) 오류 발생: greet함수만 import하였기 때문에 같은 모듈이더라도 add는 사용 할 수 없음

## 실행결과
#   Hello, Python!
