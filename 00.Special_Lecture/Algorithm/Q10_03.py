## 우주선 발사 카운트 다운

# 내코드
def countDown (n) :
    print(n)
    n -= 1
    if n == 0 :
        return print("발사!!!")
    countDown(n)
    return

countDown(5)

# 강사님 코드
def countDown2(n) :
    if n == 0 :
        print('발사!!!!!!!')
    else :
        print(n)
        countDown2(n-1)

countDown2(5)