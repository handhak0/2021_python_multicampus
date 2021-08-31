# 함수 선언
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def insertNode(findData, insertData) :
    global memory, head, current, pre
    if head.data == findData
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    node = Node() # 마지막 노드에 삽입
    node.data = insertData
    current.link = node
    return

def deleteNode(deleteData) :
    global memory, head, current, pre
    if head.data == deleteData :
        current = head
        head = head.link
        del(current)
        return
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return


    pass