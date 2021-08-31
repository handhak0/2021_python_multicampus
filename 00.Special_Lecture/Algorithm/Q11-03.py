## 선택 정렬하라.



## -100부터 100까지 숫자를 랜덤하게 30개 만들기
## 내림차순으로 정렬하기


# 함수
def SortDesc(ary) :
    n = len(ary)
    for i in range(0, n-1) :
        maxIndex = i # maxindex를 꼭 여기서 바꿔줘야 함!!!!!!!!!! 안그러면 꼭 중간에 이상하게 음수값이 제대로 정렬 안됨
        for j in range(i, n) :
            if ary[j] > ary[maxIndex] :
                maxIndex = j
        ary[i], ary[maxIndex] = ary[maxIndex], ary[i]
    return ary


# 전역 변수
import random
dataAry = [random.randrange(-100,100) for _ in range(30)] # check

# 메인
print('전 -->', dataAry)
SortDesc(dataAry)
print('후 -->', dataAry)
