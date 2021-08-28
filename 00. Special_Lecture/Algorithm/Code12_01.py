# 검색

# 함수
def SearchAry(ary, value) :
    pos= -1
    start = 0
    end = len(ary) - 1

    while start <= end :
        mid = (start + end)//2
        if value == ary[mid] :
            return mid
        elif value >= ary[mid] :
            start = mid + 1 # 중앙의 오른쪽으로
        else :
            end = mid -1 # 중앙의 왼쪽으로
    return pos

# 전역변수
dataAry = [141, 150, 162, 165, 170, 177, 180, 184]
finddata = 177

# 메인

position = SearchAry(dataAry, finddata)
if position == -1 :
    print('못찾음')
else :
    print(finddata, '는 ', position, '위치에 있음')
