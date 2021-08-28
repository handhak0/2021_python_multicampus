# 개선된 선택정렬 (한 개의 배열만 사용)

import random

## 함수

def selectionSort(ary) :
    n = len(ary)
    for i in range(0,n-1) :
        minIndex = i
        for j in range(i+1, n) :
            if ary[minIndex] > ary[j] :
                minIndex = j

        ary[i], ary[minIndex] = ary[minIndex], ary[i] # 자리 바꾸기

    return ary



## 전역
dataAry = [random.randint(33,190) for _ in range(20)] # randrange도 됨


## 메인
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry )