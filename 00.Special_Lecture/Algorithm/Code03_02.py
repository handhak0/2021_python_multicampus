# 데이터 삽입 구현

katok = ['a','b','c','d','e']

def insert_data(position, friend) : # 삽입 함수
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

insert_data(2, '솔라') # 2등 위치에 솔라를 넣어라
print(katok)
insert_data(6, '문별') # 6등 위치에 문별을 넣어라
print(katok)






