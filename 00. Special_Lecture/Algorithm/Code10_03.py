# 10부터 1까지의 합계 재귀호출로 구현

def addnum(num) :
    if num <= 1 : # 그만하는 위치
        return 1
    return num + addnum(num-1)

# 메인

print(addnum(5))