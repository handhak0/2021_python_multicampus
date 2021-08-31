# 재귀 호출

# 함수
def openBox() :
    global count
    print('상자 열기~')
    count -= 1
    if count == 0 : # 그만하는 위치
        print('** 선물 넣기 **')
        return
    openBox() # 함수 열기
    print('~~ 상자 닫기') # 함수가 닫히고 이거 출력

## 전역

count = 5

## 메인
openBox()