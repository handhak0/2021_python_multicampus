### 선형 리스트 시작



katok = [] # 빈 배열

katok.append(None) # 빈 칸 추가
katok[0] = '다현'

katok.append(None) # 빈 칸 추가
katok[1] = '정연'

# 친구 추가 함수 만들기
katok = [] # 빈 배열
def add_data(friend) :
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend # 마지막 칸에다가 추가

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')


print(katok)

