katok = ['a','b','c','d','e']

def delete_dat(position) :
    kLen = len(katok)
    katok[position] = None # 원하는 위치의 등수를 지움

    for i in range(position+1, kLen, 1) :
        katok[i-1] = katok[i]
        katok[i] = None

    del (katok[kLen-1]) # 비어있는 마지막 칸은 지우기

delete_dat(1)
print(katok)