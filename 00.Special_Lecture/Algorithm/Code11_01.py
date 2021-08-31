# 선택정렬

def findMinIndex(ary) :
    minIndex = 0
    for i in range(1, len(ary)) :
        if ary[i] < ary[minIndex] :
            minIndex = i

    return minIndex

testAry = [55, 88, 33, 77]

print(testAry[findMinIndex(testAry)])


