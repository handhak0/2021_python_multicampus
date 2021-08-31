import random

## 함수

def findMinIndex(ary) :
    minIndex = 0
    for i in range(1, len(ary)) :
        if ary[i] < ary[minIndex] :
            minIndex = i

    return minIndex

## 전역
before = [random.randint(33,190) for _ in range(20)] # randrange도 됨

after = []

## 메인
print('정렬 전 -->', before)



# before 개수만큼 반복
for _ in range(len(before)) :
    temp = findMinIndex(before) # 가장 작은 위치를 알아내기
    after.append(before[temp]) # 가장 작은 값을 after에 넣은 후,
    del before[temp] # before에서는 지우기


print('정렬 후 -->', after )


## 지금은 배열을 2개 쓰지만 원래는 1개로만 써야 하는 것이 좋다

