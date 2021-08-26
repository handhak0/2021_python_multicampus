## 함수 선언부
def add_data(friend) :
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend # 마지막 칸에다가 추가

def insert_data(position, friend) : # 삽입 함수
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_dat(position) :
    kLen = len(katok)
    katok[position] = None # 원하는 위치의 등수를 지움

    for i in range(position+1, kLen, 1) :
        katok[i-1] = katok[i]
        katok[i] = None

    del (katok[kLen-1]) # 비어있는 마지막 칸은 지우기

## 전역 변수부

katok = []
select = -1 # 1추가 2삽입 3삭제 4종료


## 메인 코드부

while (select != 4) :
    select = int(input("1추가 2삽입 3삭제 4종료  -->"))

    if (select == 1) :
        friend = input("추가할_친구 -->")
        add_data(friend)

    elif (select == 2) :
        position = int(input("삽입할_위치 -->"))
        friend = input("추가할_친구 -->")
        insert_data(position, friend) # 삽입 작동

    elif (select == 3) :
        position = int(input("삭제할_위치 -->"))
        delete_dat(position)

    elif (select == 4) :
        print(katok)
        break
    else :
        print('다시 확인')
        continue