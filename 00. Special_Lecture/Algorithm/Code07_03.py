# 원형 큐 구현하기
def isQueueFull() : # 큐가 가득찼는가?
    global SIZE, queue, front, rear
    if ( (rear+1) % SIZE == front) :
        return True
    else :
        return False

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if(isQueueFull()) :
        print('큐 꽉~')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
print('<--', queue, '<--')
enQueue('선미')
print('<--', queue, '<--')
#
data = deQueue(); print('디큐 :', data)
data = deQueue(); print('디큐 :', data)
print('<--', queue, '<--')
#
enQueue('재남')
print('<--', queue, '<--')
enQueue('강아지')
print('<--', queue, '<--')
enQueue('냥이')
print('<--', queue, '<--')
