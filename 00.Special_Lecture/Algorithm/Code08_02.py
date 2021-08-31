# 이진 "탐색" 트리의 생성

## 함수
class TreeNode() :
    def __init__(self):
        self.left = None # 왼쪽 링크
        self.data = None
        self.right = None  # 오른쪽 링크


## 전역변수
memory = []
root = None # root만 알면 다 연결된다
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스'] # 데이터


## 메인

### 첫 번째 노드만 따로 만들고 나머지 애들은 똑같이 만든다
node = TreeNode()
node.data = nameAry[0]
root = node # 첫 번째 데이터를 루트로 지정
memory.append(node)

for name in nameAry[1:] : # 나머지 노드 생성
    node = TreeNode()
    node.data = name

    current = root # 루트부터 시작해서 작으면 왼쪽, 크면 오른쪽 (여기선 ㄱㄴㄷ 순)
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else : # 일단은 같은 데이터가 없다고 치고 하는 것
            if current.right == None :
                current.right = node
                break
            current = current.right


    memory.append(node)

print("이진 탐색 트리 완성")


## 이진탐색트리 검색 해보기

findData = '마마무'
current = root

# 찾을 때까지 돌려야 함 , 없을 수도 있음
while True :
    if current.data == findData :
        print(findData, "찾았당")
        break
    elif findData < current.data :
        if current.left == None : # 비어있으면 없는 거지~
            print(findData, "못찾음")
            break
        current = current.left
    else :
        if current.right == None : # 비어있으면 없는 거지~2
            print(findData, "못찾음")
            break
        current = current.right





