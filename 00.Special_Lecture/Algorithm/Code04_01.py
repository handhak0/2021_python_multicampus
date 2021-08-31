# 노드 구조 생성

class Node() :
    def __init__(self):
        self.data = None
        self.link = None


node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '졍연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

# print(node1.data, end ='')
# print(node1.link.data, end = '')
# print(node1.link.link.data)

# 단순 연결 리스트의 간단 구현

current = node1
print(current.data, end = ' ')

while (current.link != None) :
    current = current.link
    print(current.data, end=' ')