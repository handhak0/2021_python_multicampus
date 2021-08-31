## 함수 선언부
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(current) :
    print(current.data, end = ' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')

## 전역 변수부
memory = [] # 노드를 저장할 공간
head, current, pre = None, None, None
dataArray = ['a','b','c','d','e'] # 다룰 데이터

## 메인 코드부

node = Node() # 첫 번째 노드
node.data = dataArray[0]
head = node # head 지정
memory.append(node) # 연결리스트 완성

for data in dataArray[1:] :
    pre = node # 이전 노드
    node = Node() # 새로운 노드
    node.data = data
    pre.link = node
    memory.append(node)


printNodes(head)